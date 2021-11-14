from django.urls import path
from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', views.registration, name='register'),
    path('profile/<str:pk>/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logingout/', views.logout_view, name='logout'),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]