from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required
from users.decorators import teacher_required
from .forms import LeaveForm
from .models import Leave
# Create your views here.


@login_required
@teacher_required
def apply_for_leave(request):
            form.save()
    context = {'form':form, 'title': 'Apply for leave'}
    return render(request, 'leave.html', context=context)