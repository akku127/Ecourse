from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .models import Category, Course, LikeCourse, videos


# Create your views here.

def home(request):
    print('hello world')
    courses = Course.objects.order_by('-likes')
    return render(request, 'app1/index.html', {'courses': courses})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'app1/category.html', {'categories': categories})


def categoryview(request, slug):
    print(slug)
    category = Category.objects.get(slug=slug)
    courses = Course.objects.filter(category=category)
    return render(request, 'app1/catview.html', {'courses': courses})


def courseview(request, slug):
    like_status = "Like"
    course = Course.objects.get(slug=slug)
    print("likes", course.likes.all().count())
    likes = course.likes.all().count()
    if request.user in course.likes.all():
        print('user present')
        like_status = "Liked"
    else:
        print('user not present')
    num = course.num_of_vids
    print('num', num)
    vids_list = []
    for i in range(num):
        vid = videos.objects.get(course=course, num=i)
        print(vid.title)
        vids_list.append(vid)
    for v in vids_list:
        print(v.num)
        print(v.videofile)

    return render(request, 'app1/course.html', {'course': course, 'likes': likes, 'like_status': like_status, 'vids': vids_list})


def likecourse(request, slug):
    course = Course.objects.get(slug=slug)
    user = User.objects.get(id=request.user.id)
    status = ""
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
                course.likes.add(user)
                status = "liked"
            else:
                obj.value = 0
                print(obj.value)
                obj.save()
                print('Unliked')
                course.likes.remove(user)
                status = "unliked"
    except Exception as e:
        print(e)
        obj = LikeCourse.objects.create(course=course, user=user, value=1)
        print('added to table')
        print('liked')
    return redirect('courseview', slug=slug)


