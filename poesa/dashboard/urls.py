from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('onboarded/', views.onboarded),
    path('company/', views.companylist),
    path('company/<str:id>/', views.companydetail),
    path('company/create/', views.companycreate),
    path('company/delete/', views.companydelete),
]
