from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.utils import decorators
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import (
    TranscriptAttribute, Request, Transcript
    )
from .form import TranscriptRequestForm
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


def view_requests_transcripts(request, pk):
    req = Transcript.objects.get(pk=pk)
    context = {'req':req}
    return render(request, 'requests/types/transcript.html', context=context)