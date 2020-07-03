from django.db.models import *
from rest_framework import viewsets
from .serializers import *
from .models import User
from django.shortcuts import render

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.all()
    serializer_class = ActivitySerializer


class AnsViewSet(viewsets.ModelViewSet):
    queryset = ActivityPeriod.objects.select_related('user').all()
    serializer_class = AnsSerializer

