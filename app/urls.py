from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = 'My App'

urlpatterns = [
    path('', views.index),
]
