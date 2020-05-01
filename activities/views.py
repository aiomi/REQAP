from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
#from django.core import serializers
#from django.core.serializers.json import DjangoJSONEncoder

from .models import (
    TranscriptAttribute, Request, Transcript,
    Note
    )

from users.models import Staff
from .form import TranscriptRequestForm, NoteForm

from users.decorators import (
    user_is_student_or_acadoffice_staff, academic_office_staff_only
    )

import json
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
            #req.request.user = request.user
            req.save()
            messages.success(request, 'Your request for Transcript has been successful')
            return redirect('homepage')
    form = TranscriptRequestForm(None)
    context = {'Title':"Transcript Request", 'form':form}
    return render(request, 'requests/make_request.html', context=context)


def get_transcript_amount(request):

    if request.is_ajax():
        ttype = request.POST.get('transcipt_type')
        amount = TranscriptAttribute.objects.get(transcript_type=ttype).amount
        return HttpResponse(amount)
    return HttpResponse('none')

@login_required
@user_is_student_or_acadoffice_staff
def view_request_transcript(request, pk):
    req = Transcript.objects.get(pk=pk)
    form = NoteForm()
    context = {'req':req, 'form':form}
    return render(
        request, 'requests/transcript/view_transcript_request.html',
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
        r = Transcript.objects.filter(has_paid=True)[:10]
        for i in range(len(r)):
            for j in r:
                print(i, j.transcript_type)
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

@login_required
@academic_office_staff_only
def respond_to_transcript_request(request):
    """
    either a transcript request is accepted or rejected,
    either way we handle both cases
    """
    if request.is_ajax():
        
        request_instance = Request.objects.get(id=int(request.POST.get('req_id')))
        staff_instance = Staff.objects.get(id = request.user.staff.id) 
        Note.objects.create(
            request= request_instance,
            action = request.POST.get('action'),
            reason = request.POST.get('reason'),
            staff_id = staff_instance
        )
        print(request.POST)

        return JsonResponse(data={'response':'successful'})
