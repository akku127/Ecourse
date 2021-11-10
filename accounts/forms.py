from app1.models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm

from accounts.models import *

class NewUserForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')
