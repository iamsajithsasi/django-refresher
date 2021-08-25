from django.shortcuts import render
from django.template import response

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def onboarded(request):
    res = "onboarded"
    return Response(res)

@api_view(["GET"])
def companylist(request):
    res = "list"
    return Response(res)

@api_view(["GET"])
def companydetail(request):
    res = "detail"
    return Response(res)

@api_view(["GET"])
def companycreate(request):
    res = "create"
    return Response(res)

@api_view(["GET"])
def companydelete(request):
    res = "delete"
    return Response(res)
