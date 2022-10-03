from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('pars/', views.pars_film),
    path('<int:pk>/', views.info),
    path('comments/<int:pk>', views.get_comments),
    path('account/', include('user.urls')),
]
