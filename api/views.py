from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ListSerializer
from .models import ListModel

# Create your views here.
@api_view(['GET'])
def index(request):
    api_urls = {
        "List": "list/",
        "Detail": "details/<str:pk>/",
        "Create": "create/",
        "Update": "update/<str:pk>/",
        "Delete": "delete/<str:pk>/",
    }
    return Response(api_urls)

@api_view(['GET'])
def ListView(request):
    list = ListModel.objects.all()
    serializer = ListSerializer(list, many=True)
    return Response(serializer.data)