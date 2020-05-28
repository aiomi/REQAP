from django.shortcuts import render, redirect, reverse

from .forms import LeaveForm
from .models import Leave
# Create your views here.


def apply_for_leave(request):
    form = LeaveForm()
    if request.method=="POST":
        if form.is_valid():
            form = LeaveForm(request.POST or None)
            form.save()
    context = {'form':form}
    return render(request, 'leave.html', context=context)