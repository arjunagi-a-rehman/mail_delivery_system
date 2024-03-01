from django.contrib import admin
from .models import User,JobSchedule
# Register your models here.

class UserAdmin(admin.ModelAdmin):
  list_display=('name','email','isSubscribed')

class JobScheduleAdmin(admin.ModelAdmin):
  list_display=('name','frequency','starting')

admin.site.register(User,UserAdmin)
admin.site.register(JobSchedule,JobScheduleAdmin)
