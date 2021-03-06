from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.

# Category Table
class Category(models.Model):
    name = models.CharField(max_length=150)
    slug = models.SlugField(max_length=50, null=True, blank=True)
    thumbnail = models.ImageField(upload_to='category_bgimage', null=True, blank=True)

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
    about = models.CharField(max_length=900, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=150, blank=True, null=True)
    lecturer = models.CharField(max_length=150, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True, editable=True)
    date_modified = models.DateField(auto_now=True, null=True, blank=True, editable=True)
    thumbnail = models.ImageField(upload_to='thumbnails', null=True, blank=True)
    likes = models.ManyToManyField(User, blank=True)
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


class video(models.Model):
    title = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    num = models.IntegerField()
    videofile = models.FileField(upload_to='videos', null=True, blank=True)
    likes = models.ManyToManyField(User)

    def __str__(self):
        return self.title + " " + str(self.num)


class Comment(models.Model):
    text = models.TextField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(video, on_delete=models.CASCADE, null=True, blank=True, related_name="commentrelname")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.text + " " + str(self.user)


# Likes table
class LikeCourse(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.IntegerField(default=0)
    video = models.ForeignKey(video, related_name='vidrelname', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        heading = str(self.course) + " " + str(self.user) + " " + str(self.value)
        return heading


class Subscription(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_subscribed = models.DateTimeField(auto_now_add=True)
    date_unsubscribed = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return str(self.user) + "-" + str(self.course)
