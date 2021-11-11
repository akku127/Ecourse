from app1.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import *

class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('user', 'dob', 'address', 'city', 'country', 'phone', 'picture', 'is_student', 'is_lecturer')
        widgets = {
            'dob': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'user': forms.HiddenInput(),
            'is_student': forms.HiddenInput(),
            'is_lecturer': forms.HiddenInput(),
        }