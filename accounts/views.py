from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewUserForm, UserProfileForm
from django.contrib import messages

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
            # messages.success("User Created, Please complete the profile now")
            email = form.cleaned_data['email']
            print(email)
            user = User.objects.get(email=email)
            print(user)
            return redirect('profile', pk=user.id)
        else:
            print(form.errors)

    else:
        form = NewUserForm()
    return render(request, 'accounts/registration.html', {'form': form})

def profile(request, pk):
    user = User.objects.get(id=pk)
    print(user)
    if request.method == 'POST':

        form = UserProfileForm(request.POST)
        print(user)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = user
            instance.save()
            print('form saved')
        else:
            print('jumped to else')
            print(form.errors)
    else:
        form = UserProfileForm()
        print(form)
    return render(request, 'accounts/profile_completion.html', {'form': form})
