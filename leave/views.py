from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from users.decorators import teacher_required
from .forms import LeaveForm
from .models import Leave
# Create your views here.



@login_required
@teacher_required
def apply_for_leave(request):
    form = LeaveForm()
    if request.method=="POST":
        if form.is_valid():
            form = LeaveForm(request.POST or None)
            form.save()
    context = {'form':form}
    return render(request, 'leave.html', context=context)