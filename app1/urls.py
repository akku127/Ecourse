from django.urls import path, include
from django.conf.urls import url

from .import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('catview/<slug:slug>/', views.categoryview, name='categoryview'),
    path('course/<slug:slug>/', views.courseview, name='courseview'),
    path('like/<slug:slug>/', views.likecourse, name='likecourse'),
    path('subscribe/<slug:slug>/', views.subscribe, name='subscribe'),
    path('completed/<slug:slug>/', views.completed_course, name='complete_btn')
    # path('addvid/', views.addvideo, name='addvideo')
]
