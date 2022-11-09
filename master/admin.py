from django.contrib import admin
from master import models
from helpers.models import Trackadmin
# Register your models here.
class Announcements(admin.ModelAdmin):
   Fields = [
        'Title',
        'Department',
        'Start_Date',
        'End_Date',
        'Summery',
        'Description',
        'status',
        'created_at',
        'updated_at',
        'id',
    ]
   list_display   = Fields
   search_fields  = Fields
   #list_filter    = Fields

admin.site.register(models.Announcements,Announcements)

class Blood(admin.ModelAdmin):
      Fields    = [
        'Blood_Group',
        'status',
        'created_at',
        'updated_at',
        'id',
      ]
      list_display   = Fields
      search_fields  = Fields
      #list_filter    = Fields
admin.site.register(models.Blood,Blood)

class Countries(admin.ModelAdmin):
      Fields = [
        'Sort_Name',
        'Country_Name',
        'Phone_Code',
        'id',
      ]
      list_display   = Fields
      search_fields  = Fields
      #list_filter    = Fields
admin.site.register(models.Countries,Countries)

class Departments(admin.ModelAdmin):
      Fields    = [
        'Department_Name',
        #'Department_Head',
        'status',
        'created_at',
        'updated_at',
        'id',
      ]
      list_display   = Fields
      search_fields  = Fields
      #list_filter    = Fields
admin.site.register(models.Departments,Departments)

class Designation(admin.ModelAdmin):
      Fields    = [
        'Department_Name',
        'Designation',
        'Description',
        'status',
        'created_at',
        'updated_at',
        'id',
      ]
      list_display   = Fields
      search_fields  = Fields
      #list_filter    = Fields
admin.site.register(models.Designation,Designation)

class Gender(admin.ModelAdmin):
      Fields    = [
        'Gender',
        'status',
        'created_at',
        'updated_at',
        'id',
      ]
      list_display   = Fields
      search_fields  = Fields
      #list_filter    = Fields
admin.site.register(models.Gender,Gender)

class Martial(admin.ModelAdmin):
      Fields    = [
        'Martial',
        'status',
        'created_at',
        'updated_at',
        'id',
      ]
      list_display   = Fields
      search_fields  = Fields
      #list_filter    = Fields
admin.site.register(models.Martial,Martial)

class Policies(admin.ModelAdmin):
      Fields    = [
        'Title',
        'Description',
        'Attachement',
        'status',
        'created_at',
        'updated_at',
        'id',
      ]
      list_display   = Fields
      search_fields  = Fields
      #list_filter    = Fields
admin.site.register(models.Policies,Policies)

class State(admin.ModelAdmin):
      Fields    = [
        'State_Name',
        'Country_Name',
        'id',
      ]
      list_display   = Fields
      search_fields  = Fields
      #list_filter    = Fields
admin.site.register(models.State,State)

class Shift(admin.ModelAdmin):
      Fields    = [
        'Shift_Type',
        'Start_Time',
        'End_Time',
        'status',
        'created_at',
        'updated_at',
        'id',
      ]
      list_display   = Fields
      search_fields  = Fields
      #list_filter    = Fields
admin.site.register(models.Office_Shift,Shift)