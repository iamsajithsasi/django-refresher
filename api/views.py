from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import ListSerializer
from .models import ListModel
from api import serializers

# Create your views here.
@api_view(['GET'])
def index(request):
    api_urls = {
        "List": "list/",
        "Detail": "list/<str:id>/",
        "Create": "create/",
        "Update": "update/<str:id>/",
        "Delete": "delete/<str:id>/",
    }
    return Response(api_urls)

@api_view(['GET'])
def ListView(request):
    list = ListModel.objects.all()
    serializer = ListSerializer(list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def DetailView(request, id):
    list = ListModel.objects.get(id=id)
    serializer = ListSerializer(list, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateView(request):
    serializer = ListSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['GET', 'POST'])
def UpdateView(request, id):
    list = ListModel.objects.get(id=id)
    serializer = ListSerializer(instance = list, data = request.data)

    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteView(request, id):
    list = ListModel.objects.get(id=id)
    list.delete()

    return Response("Item deleted success.")