from django.db import models
from django.contrib.auth.models import User
from app1.models import *
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    dob = models.DateField()
    created_on = models.DateField(auto_now_add=True)
    address = models.TextField(max_length=200)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    is_student = models.BooleanField(default=True)
    is_lecturer = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="profile_pics")

    def get_post(self):
        if self.is_lecturer == True:
            return "Lecturer"
        else:
            return "Student"

    def __str__(self):
        return str(self.user.first_name) + " - " + str(self.get_post())


class subscriptions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subscribed_on = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.user) + " " + str(self.course) + " " + str(self.subscribed_on)
