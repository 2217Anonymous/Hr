from django.contrib import admin
from settings import models

class Company_Tabel(admin.ModelAdmin):
    list_display    = ('Company_Name','Contact_Person','Email','Phone_Number','Website_URL')
admin.site.register(models.Company_Setting,Company_Tabel)

class Theme(admin.ModelAdmin):
    list_display    = ('Web_Name', 'Logo', 'Favicon', 'Login')
admin.site.register(models.Theme_Settings,Theme)

class Localization(admin.ModelAdmin):
    list_display    = ['Country','Date_Format','Timezone','Language','Currency_Code','Currency_Symbol']
admin.site.register(models.Localization,Localization)

class Email_Setting(admin.ModelAdmin):
    list_display    = ['Name','Sender_Email','Sender_Name','SMTP_Host','SMTP_User','SMTP_Password','SMTP_Port','Default_Server']
admin.site.register(models.Email_Setting,Email_Setting)

class Noti(admin.ModelAdmin):
    list_display    = ['Employee','Holidays','Leaves','Events','Chat','Jobs']
admin.site.register(models.Noti,Noti)

class Leaves(admin.ModelAdmin):
    list_display    = ['Leave','Days']
admin.site.register(models.Leaves,Leaves)

class Role(admin.ModelAdmin):
    list_display    = ['Roles','Grant_Employee', 'Em_Create','Em_Write', 'Em_Read', 'Em_Delete', 'Grant_Holidays', 'H_Create','H_Write', 'H_Read', 'H_Delete', 'Grant_Leaves', 'L_Create','L_Write', 'L_Read', 'L_Delete', 'Grant_Events', 'E_Create','E_Write', 'E_Read', 'E_Delete', 'Grant_Chat', 'C_Create','C_Write', 'C_Read', 'C_Delete', 'Grant_Jobs','J_Create','J_Write', 'J_Read', 'J_Delete']
admin.site.register(models.Role,Role)

class Salary(admin.ModelAdmin):
    list_display    = ['DA_HRA','DA','HRA', 'PF', 'Emp_Share', 'Org_Share', 'ESI', 'E_Share', 'O_Share']
admin.site.register(models.Salary,Salary)    

class Office(admin.ModelAdmin):
    list_display    = ['In','Out']
admin.site.register(models.Office_Time,Office) 




