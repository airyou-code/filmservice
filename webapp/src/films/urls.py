from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.search_film),
    path('search_f/', views.search_f, name='search_f'),
    path('<int:pk>/', views.info),
    path('comments/<int:pk>', views.get_comments),
]