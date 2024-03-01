from django.db import models
from enum import Enum

class User(models.Model):
  user_id=models.AutoField(primary_key=True)
  name=models.CharField(max_length=50)
  email=models.CharField(max_length=50)
  isSubscribed=models.BooleanField(default=False)
  created_at=models.DateTimeField(auto_now=True)
  active=models.BooleanField(default=True)

class Frequency(Enum):
  DAILY = 'daily'
  WEEKLY = 'weekly'
  YEARLY='yearly'
  ONCE='ONCE'



class JobSchedule(models.Model):
  jobSchedule_id=models.AutoField(primary_key=True)
  name = models.CharField(max_length=100)
  frequency = models.CharField(max_length=20, choices=[(tag.value, tag.name) for tag in Frequency]) 
  starting = models.DateTimeField()
  

  def _str_(self):
    return self.name