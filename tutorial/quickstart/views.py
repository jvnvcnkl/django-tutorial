from django.shortcuts import render

# Create your views here.

from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer

class UserViewSet(viewsets.ModelViewSet) :
    queryset= User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permissions_classes= [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
     queryset= Group.objects.all()
     serializer_class = GroupSerializer
     permissions_classes = [permissions.IsAuthenticated]