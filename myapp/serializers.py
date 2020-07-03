#serializers.py

from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz')


class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class AnsSerializer(UserSerializer):
    user = UserSerializer

    class Meta:
        model = ActivityPeriod
        fields = ('user', 'start_time', 'end_time')
