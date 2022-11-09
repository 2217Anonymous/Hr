from django import forms
from settings import models

Country= [
    ('India', 'India'),
    ('Pakistan', 'Pakistan'),
    ('Srilanga', 'Srilanga'),
    ('Austrlia', 'Austrlia'),
    ]
State= [
    ('Tamilnadu', 'Tamilnadu'),
    ('Kerala', 'Kerala'),
    ('Karnataka', 'Karnataka'),
    ('Delhi', 'Delhi'),
    ]
City= [
    ('Tirupur', 'Tirupur'),
    ('Madurai', 'Madurai'),
    ('Coimbatore', 'Coimbatore'),
    ('Chennai', 'Chennai'),
    ]
Date_Format= [
    ('15/05/2016', '15/05/2016'),
    ('15.05.2016', '15.05.2016'),
    ('15-05-2016', '15-05-2016'),
    ('05/15/2016', '05/15/2016'),
    ('2016/05/15', '2016/05/15'),
    ('2016-05-15', '2016-05-15'),
    ('15 May 2016', '15 May 2016'),
    ('May 15 2016', 'May 15 2016'),
    ]

Timezone = [
    ('(UTC +5:30) Antarctica/Palmer', '(UTC +5:30) Antarctica/Palmer'),
    ]

Language = [
    ('Tamil', 'Tamil'),
    ('English', 'English'),
    ('French', 'French'),
    ]

Currency_Code = [
    ('INR','INR'),
    ('USD', 'USD'),
    ('Pound', 'Pound'),
    ('EURO', 'EURO'),
    ]
Security = [
    ('None','None'),
    ('SSL', 'SSL'),
    ('TLS', 'TLS'),
    ]
status = [
    ('active', 'active'),
    ('deactive', 'deactive'),
]

class Company_Settings_Form(forms.ModelForm):   
    class Meta:
        model   = models.Company_Setting
        fields    = "__all__"

class Theme_Settings_Form(forms.ModelForm):   
    class Meta:
        model     = models.Theme_Settings
        fields    = ['Web_Name','Logo','Favicon','Login']
        widgets   = {
            'Web_Name'  : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Website name'}),
        }

class LocalizationForm(forms.ModelForm):
    class Meta:
        model   = models.Localization
        fields  = ['Country','Date_Format','Timezone','Language','Currency_Code','Currency_Symbol']
        widgets = {
            'Country'           : forms.Select(attrs={'class':'form-control  custom-select','data-placeholder':"Choose one"},choices=Country),
            'Date_Format'       : forms.Select(attrs={'class':'form-control  custom-select'},choices=Date_Format),
            'Timezone'          : forms.Select(attrs={'class':'form-control  custom-select'},choices=Timezone),
            'Language'          : forms.Select(attrs={'class':'form-control  custom-select'},choices=Language),
            'Currency_Code'     : forms.Select(attrs={'class':'form-control  custom-select'},choices=Currency_Code),
            'Currency_Symbol'   : forms.TextInput(attrs={'class':'form-control','readonly':'true'}),
        }

class Email_Settings_Form(forms.ModelForm):   
    class Meta:
        model     = models.Email_Setting
        fields    = ['Name','Sender_Email','Sender_Name','SMTP_Host','SMTP_User','SMTP_Password','SMTP_Port','Default_Server']
        # widgets   = {
        # 'Name'              : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Name'}),
        # 'Sender_Email'      : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Sender Email'}),
        # 'Sender_Name'       : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Sender Name'}),
        # 'SMTP_Host'         : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter SMTP Host'}),
        # 'SMTP_User'         : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter SMTP User'}),
        # 'SMTP_Password'     : forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter SMTP Password'}),
        # 'SMTP_Port'         : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter SMTP Port'}),
        # 'Default_Server'    : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Default server'}),
        # }


class Notiform(forms.ModelForm):
    class Meta:
        model     = models.Noti
        fields    = "__all__"

class Lform(forms.ModelForm):
    class Meta:
        model     = models.Leaves
        fields    = "__all__"
        # widgets   = {
        # 'Leave'  : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Leave Type'}),
        # 'Days'   : forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Number of Days'}),
        # }

class Roleform(forms.ModelForm):
    class Meta:
        model     = models.Role
        fields    = ['Roles','Grant_Employee', 'Em_Create','Em_Write', 'Em_Read', 'Em_Delete', 'Grant_Holidays', 'H_Create','H_Write', 'H_Read', 'H_Delete', 'Grant_Leaves', 'L_Create','L_Write', 'L_Read', 'L_Delete', 'Grant_Events', 'E_Create','E_Write', 'E_Read', 'E_Delete', 'Grant_Chat', 'C_Create','C_Write', 'C_Read', 'C_Delete', 'Grant_Jobs','J_Create','J_Write', 'J_Read', 'J_Delete']

class Salaryform (forms.ModelForm):
    class Meta:
        model     = models.Salary
        fields    = ['DA_HRA','DA','HRA', 'PF', 'Emp_Share', 'Org_Share', 'ESI', 'E_Share', 'O_Share']
