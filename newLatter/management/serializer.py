from rest_framework import serializers
from .models import User,JobSchedule

class UserSerializer(serializers.HyperlinkedModelSerializer):
  user_id=serializers.ReadOnlyField()
  class Meta:
    model=User
    fields='__all__'

class JobScheduleSerializer(serializers.HyperlinkedModelSerializer):
  jobSchedule_id=serializers.ReadOnlyField()
  class Meta:
    model=JobSchedule
    fields='__all__'