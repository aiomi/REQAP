from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import User
from .forms import UserRegistrationForm

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


@login_required
def profile(request, username):
    # s_user_req means specific user requests which is all the request made
    # by the currently logged in user
    s_user_req = Request.objects.filter(user=request.user)
    requests = Request.objects.all()
    context = {'requests':requests, 'specific':s_user_req}
    return render(request, 'profile.html', context=context)

