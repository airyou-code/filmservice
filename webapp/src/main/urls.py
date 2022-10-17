from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('pars/', views.pars_film),
    path('account/', include('user.urls')),
    path('film/', include('films.urls')),
    path('movi/', views.movies_page),
]
