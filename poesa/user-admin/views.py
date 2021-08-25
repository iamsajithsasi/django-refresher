from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def useradmin(request):
    api_urls = {
        "user": "user/",
        "role": "role/",
    }
    return Response(api_urls)