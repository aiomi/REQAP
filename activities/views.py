from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.db import transaction
from django.core.exceptions import SuspiciousOperation
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from .models import (
    TranscriptAttribute, Request, Transcript,
    Note
    )
from users.models import Staff
from .form import TranscriptRequestForm, NoteForm
from users.decorators import (
    user_is_student_or_acadoffice_staff, academic_office_staff_only
    )
from libs.paystack_api import PaystackAccount
from libs.constants import TranscriptStatus
# Create your views here.

def homepage(request):
    return render(request, 'home.html')


@login_required
def request_transcripts(request):
    if request.method == "POST":
        form = TranscriptRequestForm(request.POST or None)
        if form.is_valid():
            req = form.save(commit=False)
            _ = Request.objects.create(user = request.user)
            req.request = _
            req.status = TranscriptStatus.INITIATED
            #req.request.user = request.user
            req.save()
            messages.success(request, 'Your request for Transcript has been successful')
            return redirect('homepage')
    form = TranscriptRequestForm(None)
    context = {'title':"Transcript Request", 'form':form}
    return render(request, 'requests/transcript/make_transcript_request.html', context=context)


def get_transcript_amount(request):

    if request.is_ajax() and request.method == "POST":
        ttype = request.POST.get('transcipt_type')
        amount = TranscriptAttribute.objects.get(transcript_type=ttype).amount
        return HttpResponse(amount)
    raise SuspiciousOperation()

@login_required
@user_is_student_or_acadoffice_staff
def view_request_transcript(request, pk):
    req = Transcript.objects.get(pk=pk)
    form = NoteForm()
    context = {'req':req, 'form':form, 'title':'View Transcript Request'}
    return render(
        request, 'requests/transcript/view_transcript_request.html',
        context=context)

@login_required
@csrf_protect
@transaction.atomic
def pay_for_transcript(request, pk):
    """
    processes transcript payments. Payments are processed and verified through paystack
    """
    req = Transcript.objects.get(pk=pk)
    try:
        paystack = PaystackAccount(
            settings.PAYSTACK_EMAIL, settings.PAYSTACK_PUBLIC_KEY, req.amount
            )
    except TranscriptAttribute.DoesNotExist:
        pass
    
    context = {
        'req':req,
        'paystack': paystack,
        'title':'Transcript Payment'
        }

    # process payment
    if request.method == "POST":
        if paystack.verify_transcation(request.POST['reference']):
            # change request to paid, status to paid then save it
            req.status = TranscriptStatus.PAID
            req.has_paid = True
            req.save()
            messages.success(request, "Your payment was successful. It will now be attended to by the required personnel.")
            return redirect(reverse('user-profile',kwargs={'username':request.user}))
        
        messages.error(request, 'Transaction unsuccessful. Please try again later.')
    
    return render(
        request, 'requests/payment_form.html',
        context=context)


def get_valid_transcripts_requests(request):
    """
    valid here means all transcript requests that
    payments have been made 
    """
    if request.is_ajax():
        #limit request to the first 10
        #ToDo add ordering to date_created
        transcripts = dict() 
        r = Transcript.objects.filter(status=TranscriptStatus.PAID)[:10]
        for i in range(len(r)):
            for j in r:
                # TODO add matric number to json data
                transcripts[i] = {
                    'id': j.id,
                    'transcript_type': j.transcript_type.transcript_type,
                    'amount': j.amount,
                    'address': j.address,
                    'has_paid': j.has_paid,
                    'request_by': j.request.user.get_full_name()
                    }
        return JsonResponse(transcripts)
    raise SuspiciousOperation()

@login_required
@academic_office_staff_only
def respond_to_transcript_request(request):
    """
    either a transcript request is accepted or rejected,
    either way we handle both cases
    """
    if request.is_ajax() and request.method == "POST":
        
        request_instance = Request.objects.get(id=int(request.POST.get('req_id')))
        staff_instance = Staff.objects.get(id = request.user.staff.id)
        Note.objects.create(
            request= request_instance,
            action = request.POST.get('action'),
            reason = request.POST.get('reason'),
            staff_id = staff_instance
        )
        transcript = Transcript.objects.get(request=request_instance)
        transcript.status = request.POST.get('action').lower()
        transcript.approved_by = staff_instance
        transcript.save()
        return JsonResponse(data={'response':'successful'})
    
