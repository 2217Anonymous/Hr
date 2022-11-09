from django import forms
from authentication import models
from django.contrib.auth.forms import UserCreationForm
from authentication import models as auth

# class LoginForm(forms.ModelForm):
#     class Meta:
#         model = models.User
#         fields = ['username','password']

class Employee_RegisterForm(UserCreationForm):
    class Meta:
        model  = auth.User
        fields = [
        'Employee_Id',
        'Profile_Pic',
        'username',
        'password1',
        'password2',
        'first_name',
        'last_name',
        'email',
        'Phone',
        'Gender',
        'Department',
        'Designation',
        'Date_Of_Joining',
        'Resignation_Dt',
        'Termination_Dt',
        'Shift_Type',
        'Salary',
        'is_employee',
        'is_admin',
        'is_client',
            ]

        # def __str__(self):


