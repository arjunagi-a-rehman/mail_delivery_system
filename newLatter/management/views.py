from django.shortcuts import render
from rest_framework import viewsets
from .models import User,JobSchedule
from .serializer import UserSerializer,JobScheduleSerializer
# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
  queryset=User.objects.all()
  serializer_class=UserSerializer

class JobScheduleViewSet(viewsets.ModelViewSet):
  queryset=JobSchedule.objects.all()
  serializer_class=JobScheduleSerializer