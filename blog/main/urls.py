from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('pars/<int:idkino>', views.pars),
    path('<int:pk>/', views.info)
]
