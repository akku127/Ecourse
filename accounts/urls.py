from django.urls import path
from .import views
urlpatterns = [
    path('', views.registration, name='registration'),
    path('profile/<str:pk>/', views.profile, name='profile'),
]