from django.urls import path
from settings import views

urlpatterns = [ 
    path('',views.Settings,name="settings"),
    path('company-settings/', views.Company_settings, name='company-settings'),
    path('theme/',views.Theme,name="theme"),
    path('localization/', views.Localization, name='localization'),
    path('email-settings/', views.Email_settings, name='email-settings'),
    path('email-edit/', views.Email_Edit, name="email-edit"),
    path('email-delete/<int:id>', views.Email_Delete, name="email-delete"),
    path('notification/', views.Notification, name="notification"),
    path('leave/', views.Leave, name="leave"),
    path('leave-edit/', views.Leave_Edit, name="leave-edit"),
    path('leave-delete/<int:id>', views.Leave_Delete, name="leave-delete"),
    path('permission/', views.Permission, name='permission'),
    path('salary-settings/', views.Salary_Settings, name='salary-settings'),
]
