from django.shortcuts import render, redirect

from .models import User
from .forms import UserRegistrationForm
# Create your views here.

def register(request):
    form = UserRegistrationForm()
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST or None)
        form.save()
        return redirect('login')
    context = {'form':form}
    return render(request, 'registration/register.html', context=context)


