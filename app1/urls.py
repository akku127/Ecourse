from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('categories/', views.categories, name='categories'),
    path('<slug:slug>', views.categoryview, name='categoryview'),
    path('course/<slug:slug>/', views.courseview, name='courseview'),
    path('like/<slug:slug>/', views.likecourse, name='likecourse'),
]
