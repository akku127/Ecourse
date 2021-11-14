from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import NewUserForm, UserProfileForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib import messages


# Create your views here.

@login_required()
def dashboard(request):
    print(request.user)
    user_profile = Profile.objects.get(user=request.user)
    subs = Subscription.objects.filter(user=request.user)
    return render(request, 'accounts/dashboard.html', {'profile': user_profile, 'subs': subs})


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
    return render(request, 'accounts/registration.html', {'form': form, 'title': "Registration Form"})


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
            messages.success(request, "Updated Profile")
            return redirect('home')
        else:
            print('jumped to else')
            print(form.errors)
            messages.error(request, "Unsuccessfull Profile Updation")
            return redirect('home')
    else:
        form = UserProfileForm()
        print(form)
    return render(request, 'accounts/profile_completion.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Successfully Logged in")
            if "next" in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
        else:
            print(form.errors)
            print("login Error")
            messages.error(request, "Login error")
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form, 'title': "Login"})


def logout_view(request):
    print(request.user)
    if request.method == 'POST':
        logout(request)
        print("logged Out")
        messages.success(request, "Logged Out")
        return redirect('home')
    else:
        print('Get request to logout view')
        return redirect('home')
