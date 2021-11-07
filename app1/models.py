from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.

# Category Table
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('categoryview', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


# Course Table
class Course(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    lecturer = models.CharField(max_length=150, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=True)
    date_modified = models.DateField(auto_now=True, null=True, blank=True, editable=True)
    thumbnail = models.ImageField(upload_to='thumbnails', null=True, blank=True)
    likes = models.ManyToManyField(User, related_name='course_like', blank=True, null=True)
    num_of_vids = models.IntegerField(null=True, blank=True)
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    def get_absolute_url(self):
        return reverse('courseview', kwargs={'slug': self.slug})

    def get_likes(self):
        return self.likes

# Likes table
class LikeCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(max_length=2, default=0)

    def __str__(self):
        heading = str(self.course) + " " + str(self.user) + " " + str(self.value)
        return heading

class videos(models.Model):
    title = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    num = models.IntegerField()
    videofile = models.FileField(upload_to='videos', null=True, blank=True)

    def __str__(self):
        return self.title + str(self.num)

class Comment(models.Model):
    text = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    video = models.ForeignKey(videos, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text + str(self.user)
