from django.contrib import admin
from authentication import models
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class User(admin.ModelAdmin):
   model = models.User
   list_display    = [
        'id',
        'username',
        'Employee_Id',
        'email',       
        'Gender',
        'first_name',
        'last_name',
        'Phone',
        'Department',
        'Designation',
        'is_active',
        'is_employee',
        'is_admin',
        'is_client',
        'is_superuser',
        'Profile_Pic',
     ]
admin.site.register(models.User,User)


class Manager(admin.ModelAdmin):
       model = models.Manager
       list_display = [
         'id',
         'name',
         'utext',
         'email',
       ]
admin.site.register(models.Manager,Manager)
