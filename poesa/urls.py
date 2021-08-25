from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="Main"),
    path('dashboard/', include(("poesa.dashboard.urls", "dashboard"), namespace='dashboard')),
    path('admin/', include(("poesa.user-admin.urls", "user-admin"), namespace='user-admin')),
]