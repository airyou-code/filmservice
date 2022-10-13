from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.search_film),
    path('search_f/', views.search_page, name='search_f'),
    path('search_popup/', views.search_popup),
    path('<int:pk>/', views.info),
    path('comments/<int:pk>', views.get_comments),
]