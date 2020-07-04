from django.db.models import *
from rest_framework import viewsets
from .serializers import *
from .models import User
from django.shortcuts import render
from FT.response_parser import success_response, failure_response
from django.views import View

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ActivityViewSet(viewsets.ModelViewSet):
    for id in User.objects.values('id').all():
        queryset = ActivityPeriod.objects.filter( user=User.objects.get(id=id['id']) )
        serializer_class = ActivitySerializer(queryset, many=True)


class AnsViewSet(View):

    def get(self, request):
        users = User.objects.prefetch_related('activity_periods').all()
        if len(users) != 0:
            serializer = UserSerializer(users, many=True)
            return success_response("members", serializer.data)
        return failure_response("No users found in DB, run populate_db command")


# class AnsViewSet(viewsets.ModelViewSet):
#     queryset = ActivityPeriod.objects.prefetch_related('user').all()
#     serializer_class = AnsSerializer

