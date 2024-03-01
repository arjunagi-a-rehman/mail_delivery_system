from django.contrib import admin
from django.urls import path,include
from .views import UserViewSet,JobScheduleViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'users',UserViewSet)
router.register(r'jobScheduler',JobScheduleViewSet)
urlpatterns = [
    path('',include(router.urls))
]