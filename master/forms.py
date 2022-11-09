import re
from django import forms
from master import models

def name_start(value):
    if value == '':
        raise forms.ValidationError("Please Fill the details")

class Department_Form(forms.ModelForm):   
    Department_Name = forms.CharField(required=True)
    Department_Head = forms.CharField(required=True)
    status          = forms.BooleanField(required=True)
    class Meta:
        model   = models.Departments
        fields  = '__all__'

class Designation_Form(forms.ModelForm):
    Department_Name = forms.CharField(required=True)
    Designation     = forms.CharField(required=True)
    Description     = forms.CharField(required=True)
    status          = forms.BooleanField(required=True)
    class Meta:
        model   = models.Designation    
        fields  = '__all__'
