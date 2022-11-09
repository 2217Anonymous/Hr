from django import forms
from authentication import models as auth
from django.contrib.auth.forms import UserCreationForm
from employees import models as emp
from helpers import models as help
from .widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

class Employee_Details_Form(forms.ModelForm):
    class Meta:
        model   = emp.Basic_Employee    
        fields  = "__all__"

class Bank_Details_Form(forms.ModelForm):
    class Meta:
        model   = emp.Bank_Details    
        fields  = "__all__"

class Employee_Documents_Form(forms.ModelForm):
    class Meta:
        model   = emp.Documents    
        fields  = "__all__"

class Emergency_Contact_Form(forms.ModelForm):
    class Meta:
        model   = emp.Emergency    
        fields  = "__all__"

class Social_Media_Form(forms.ModelForm):
    class Meta:
        model   = emp.Social    
        fields  = "__all__"

class Leave_Request_Form(forms.ModelForm):
    class Meta:
        model   = emp.Leave
        fields  = ("user","Start_Date","End_Date","Leave_Type","Reason")

class Attendance_Form(forms.ModelForm):
    class Meta:
        model   = emp.Attendance
        fields  = ("user","In_Time","Out_Time")

class Manual_Attendance_Form(forms.ModelForm):
    class Meta:
        model = emp.Attendance
        fields  = ("user","Manual_Dt","In_Time","Out_Time","Reason")

        widgets = {
            'In_Time' : TimePickerInput(),
            'Out_Time' :TimePickerInput(),
        }