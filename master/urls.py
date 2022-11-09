from django.urls import path
from master import views

urlpatterns = [
    path('department/',views.Department,name="department" ),
    path('dept-delete/<int:id>',views.Dept_Delete,name="dept-delete"),
    path('dept-edit/',views.Dept_Edit,name="dept-edit"),
    path('designation/',views.Designation,name="designation"),
    path('designation-delete/<int:id>',views.Designation_Delete,name="designation-delete"),
    path('designation-edit/',views.Designation_Edit,name="designation-edit"),
    # path('country/',views.Country,name="country"),
    # path('state/',views.States,name="state"),
    # path('blood/',views.Blood_Group,name="bl  ood"),
    # path('status/',views.Status_Type,name="status"),
    # path('gender/',views.Gender_Type,name="gender"),
    # path('martial/',views.Martial_Status,name="martial"),
]