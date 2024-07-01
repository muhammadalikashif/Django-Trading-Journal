from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.Login.as_view(), name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name="accounts/login.html"), name='login'),
    
]
