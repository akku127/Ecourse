from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .forms import CommentForm, AddVidForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Category, Course, LikeCourse, video, Comment, Subscription
from accounts.models import Profile


# Create your views here.

def home(request):
    title = "Home"
    print('hello world')
    courses = Course.objects.all().order_by('-likes')
    recently_added_courses = Course.objects.all().order_by('-date_created')[:4]
    print(recently_added_courses.count())
    return render(request, 'app1/index.html',
                  {'courses': courses, 'title': title, 'recentcourses': recently_added_courses})


def categories(request):
    categories = Category.objects.all()
    return render(request, 'app1/category.html', {'categories': categories, 'title': "Categories"})


def categoryview(request, slug):
    print(slug)
    category = Category.objects.get(slug=slug)
    courses = Course.objects.filter(category=category)
    return render(request, 'app1/catview.html', {'courses': courses, 'title': "Categories"})


@login_required(login_url='login')
def courseview(request, slug):
    course = Course.objects.get(slug=slug)
    user = request.user
    if check_subscription(course, user):
        print("subscribed he")
        subscribed = True
    else:
        print("not subscribed he")
        subscribed = False
    like_status = "Like"
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
        print('i', i)
        print('num', num)
        try:
            vid = video.objects.get(course=course, num=i)
            print(vid.title)
            vids_list.append(vid)
        except Exception as e:
            print(e)
    comment_form = CommentForm()
    complete_btn = ''
    if subscribed:
        sub = Subscription.objects.get(course=course, user=request.user)
        if sub.completed:
            complete_btn = "Mark Incomplete"
        else:
            complete_btn = "Mark Completed"
    return render(request, 'app1/course.html',
                  {'subscribed': subscribed, 'course': course, 'likes': likes, 'like_status': like_status,
                   'vids': vids_list,
                   'comment_form': comment_form, 'title': course.name, 'complete_btn': complete_btn})


@login_required(login_url='login')
def likecourse(request, slug):
    course = Course.objects.get(slug=slug)
    user = request.user
    status = ""
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
        print('entered exception in like')
        print(e)
        obj = LikeCourse.objects.create(course=course, user=user, value=1)
        obj.value = 1
        obj.save()
        print('added to table')
        print('liked')
        course.likes.add(user)
        print('added to course like')
    data = {'status': status}
    return redirect('courseview', slug=slug)


@login_required(login_url='login')
def subscribe(request, slug):
    if request.method == "POST":
        course = Course.objects.get(slug=slug)
        user = request.user
        try:
            Subscription.objects.get(user=user, course=course)
            print('subscription found')
            Subscription.objects.get(user=user, course=course).delete()
        except Exception as e:
            print('not subscrbed')
            Subscription.objects.create(user=user, course=course)
            return redirect('courseview', slug=slug)
    return redirect('home')


# @login_required(login_url='login')
# def addvideo(request):
#     profile = Profile.objects.get(user=request.user)
#     user_courses = ""
#     if profile.is_lecturer:
#         if profile.is_approved:
#             print('lecturer')
#             user_courses = Course.objects.filter(lecturer=request.user.username)
#             for c in user_courses:
#                 print(c.name)
#         else:
#             print('not approved')
#     else:
#         print('not a lecturer')
#     if request.method == 'POST':
#         print('POST request')
#         form = AddVidForm(request.POST, request.FILES)
#         if form.is_valid():
#             obj = form.save(commit=False)
#
#             obj.course = request.FILES['course']
#
#             obj.save()
#             return redirect('home')
#         else:
#             print("Form not valid")
#     else:
#         form = AddVidForm()
#     return render(request, 'app1/addvid.html', {'form': form, 'user_courses': user_courses})


def check_subscription(course, user):
    try:
        Subscription.objects.get(course=course, user=user)
        print("Has a subscription")
        return True
    except Exception as e:
        print("doesnt have subscription")
        return False


@login_required(login_url='login')
def completed_course(request, slug):
    course = Course.objects.get(slug=slug)
    sub = Subscription.objects.get(course=course, user=request.user)
    print(sub.completed)
    if sub.completed == True:
        print('already completed, marking as incomplete')
        sub.completed = False
        sub.save()
        messages.success(request, 'Marked as incomplete')
    else:
        print('completing now')
        sub.completed = True
        sub.save()
        messages.success(request, 'marked as complete')
    return redirect('courseview', slug=slug)
