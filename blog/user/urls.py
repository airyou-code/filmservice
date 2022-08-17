from django.urls import path
from . import views
from django.contrib.auth import update_session_auth_hash

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
]