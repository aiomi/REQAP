from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import User, StaffVerification
from .forms import (
    UserRegistrationForm, TeacherSignUpForm,
    StaffVerificationForm
    )

from activities.models import Request
# Create your views here.


def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        form.save()
        return redirect('login')
    context = {'form':form}
    return render(request, 'registration/register.html', context=context)

class TeacherSignUpView(CreateView):
    form_class = TeacherSignUpForm
    model = User
    template_name = 'registration/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('homepage')

class StaffVerificationView(CreateView):
    form_class = StaffVerificationForm
    model = StaffVerification
    template_name = 'registration/staff_verify.html'

    def form_valid(self, form):
        form.save()
        return redirect('homepage')

@login_required
def profile(request, username):
    # s_user_req means specific user requests which is all the request made
    # by the currently logged in user
    s_user_req = Request.objects.filter(user=request.user)
    requests = Request.objects.all()
    context = {'requests':requests, 'specific':s_user_req}
    return render(request, 'profile.html', context=context)

