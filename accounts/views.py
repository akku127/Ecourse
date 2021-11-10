from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewUserForm
# Create your views here.


# @login_required()
def dashboard(request):
    return render(request, 'accounts/dashboard.html')

def registration(request):
    if request.method == 'POST':
        print('POST')
        form = NewUserForm(request.POST)
        if form.is_valid():
            print('Valid')
            form.save()
        else:
            print(form.errors)

    else:
        form = NewUserForm()
    return render(request, 'accounts/registration.html', {'form': form})

