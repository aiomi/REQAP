from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.utils import decorators
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import (
    TranscriptAttribute, Request, Transcript,
    Note
    )
from .form import TranscriptRequestForm, NoteForm
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
def view_requests_transcripts(request, pk):
    req = Transcript.objects.get(pk=pk)
    form = NoteForm()
    context = {'req':req, 'form':form}
    return render(
        request, 'requests/transcript/view_transcript_request.html',
        context=context)

#should require only staffs from academic offices
# or staff who has permission of academic office
@login_required
def respond_to_transcript_request(request):
    """
    either a transcript request is accepted or rejected,
    either way we handle both cases
    """
    if request.is_ajax():
        #Note.objects.create()
        print(request.GET)
        print(request.POST)
        return True
    return False