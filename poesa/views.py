from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .plans import dashboardplan

# Create your views here.
@api_view(["GET"])
def index(request):
    api_urls = {
        "dashboard": dashboardplan(),
        "admin-user": {
            "list": "admin/user/",
            "detail": "admin/user/<str:id>/",
            "Create": "admin/user/create/",
            "Update": "admin/user/update/<str:id>/",
            "Delete": "admin/user/delete/<str:id>/",
        },
        "admin-role": {
            "list": "admin/role/",
            "detail": "admin/role/<str:id>/",
            "Create": "admin/role/create/",
            "Update": "admin/role/update/<str:id>/",
            "Delete": "admin/role/delete/<str:id>/",
        },
    }
    return Response(api_urls)
