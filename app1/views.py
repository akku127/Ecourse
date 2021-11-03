from django.shortcuts import render, redirect
from .models import Category, Course, LikeCourse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    print('hello world')
    return render(request, 'app1/index.html')


def categories(request):
    categories = Category.objects.all()
    return render(request, 'app1/category.html', {'categories': categories})


def categoryview(request, slug):
    print(slug)
    category = Category.objects.get(slug=slug)
    courses = Course.objects.filter(category=category)
    return render(request, 'app1/catview.html', {'courses': courses})


def courseview(request, slug):
    course = Course.objects.get(slug=slug)
    return render(request, 'app1/course.html', {'course': course})


def likecourse(request, slug):
    course = Course.objects.get(slug=slug)
    user = User.objects.get(id=request.user.id)
    # obj = LikeCourse.objects.create(course=course, user=user, value=1)
    try:
        print('try block')
        obj = LikeCourse.objects.get(course=course, user=user)
        if obj:
            print(obj.value)
            if obj.value == 0:
                print('Currently not liked')
                obj.value = 1
                obj.save()
                print('now liked')
            else:
                obj.value = 0
                print(obj.value)
                obj.save()
                print('Unliked')
    except Exception as e:
        print(e)
        obj = LikeCourse.objects.create(course=course, user=user, value=1)
        print('added to table')
    return render(request, 'app1/course.html', {'course': course})
