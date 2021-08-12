from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('list/', views.ListView),
    path('list/<str:id>/', views.DetailView),
    path('create/', views.CreateView),
    path('update/<str:id>/', views.UpdateView),
    path('delete/<str:id>/', views.DeleteView),
]
