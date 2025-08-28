from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from django.contrib.auth.models import User

from demomvc.serializer import UserSerializer

def index(request):
    return HttpResponse("Hello, world!")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
