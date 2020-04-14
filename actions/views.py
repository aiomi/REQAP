from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Request
from .forms import RequestForm
# Create your views here.

def home(request):
    return render(request, 'home.html')

@login_required
def make_request(request):
    req_form = RequestForm()
    if request.method == "POST":
        req_form = RequestForm(request.POST or None)
        req_form.save()
        return redirect('homepage')
    context = {'form':req_form}
    return render(request, 'make_request.html', context=context)
