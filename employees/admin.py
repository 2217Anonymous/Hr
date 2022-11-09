from django.contrib import admin
from . import models as employee
#Register your models here.

class Employee(admin.ModelAdmin):
    pass

class Bank(admin.ModelAdmin):
    pass

class Documents(admin.ModelAdmin):
    pass

class Emergency(admin.ModelAdmin):
    pass

class Social(admin.ModelAdmin):
    pass

class Attendance(admin.ModelAdmin):
    Fields    = [
        'user',
        'Date',
        'In_Time',
        'Out_Time',
        'Clock_In',
        'Clock_Out',
        'Late',
        'Early_Leaving',
        'Total_Working_Hours',
        'Status',
      ]
    list_display   = Fields
    search_fields  = Fields
admin.site.register(employee.Attendance,Attendance)

class Leave(admin.ModelAdmin):
    Fields = [
        'user',
        'Start_Date',
        'End_Date',
        'leave_days',
        'Leave_Type',
        'Reason',
        'Approved_Status',
        'Approved_Description',
        'is_approved',
    ]
    list_display   = Fields
    search_fields  = Fields
admin.site.register(employee.Leave,Leave)

admin.site.register(employee.Basic_Employee)
admin.site.register(employee.Bank_Details)
admin.site.register(employee.Documents)
admin.site.register(employee.Emergency)
admin.site.register(employee.Social)

