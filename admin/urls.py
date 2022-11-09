from django.contrib import admin
from django.urls import path,include
from admin import views

urlpatterns = [
    path('',views.Dashboard,name="hr-dashboard"),
    path('side',views.Side_Bar,name="side"),
]