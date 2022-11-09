from django.urls import path
from employees import views

urlpatterns = [
    path('',views.employee_dashboard,name="employee"),
    path('employee-details/',views.employee_details,name="employee-details"),
    path('employee-list/',views.employee_list,name="employee-list"),
    #path('edit-employee-details/<int:pk>',views.edit_employee_details,name="employee-details"),
    path('delete-employee-details/<int:pk>',views.delete_employee_details,name="delete-employee-details"),
    path('bank-details/',views.bank_details,name="bank-details"),
    path('edit-bank-details/',views.edit_bank_details,name="edit-bank-details"),
    path('delete-bank-details/<int:pk>',views.delete_bank_details,name="delete-bank-details"),
    path('employee-documents',views.emp_documents,name="employee-documents"),
    path('delete-employee-documents/<int:pk>',views.delete_emp_documents,name="delete-employee-documents"),
    path('emergency-contact/',views.emg_contact,name="emergency-contact"),
    path('delete-emergency-contact/<int:pk>',views.delete_emg_contact,name="delete-emergency-contact"),
    path('social-media/',views.social_media,name="social-media"),
    path('delete-social-media/<int:pk>',views.delete_social_media,name="delete-social-media"),

    path('leave/',views.leave,name="leave"),
    path('leave-request/',views.leave_request,name="leave-request"),
    path('leave-application/',views.leave_application,name="leave-application"),
    path('leave-approval/',views.leave_approval,name="leave-approval"),
    #path('leave-rejected/<int:pk>',views.leave_rejection,name="leave-rejected"),

    path('attendance/',views.attendance,name="attendance"),
    path('In/',views.In,name="In"),
    path('Out/',views.Out,name="Out"),
    path('attendance-list',views.attendance_list,name="attendance-list"),
    path('employee-attendance',views.employee_attendance,name="employee-attendance"),
    path('manual-attendance/',views.manual_attendance,name="manual-attendance"),
]

