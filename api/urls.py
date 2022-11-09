from django.urls import path,include
from .authentication.views import UsersView
from .master.views import DepartmentView,DesignationView,BloodView,MartialView,GenderView,PoliciesView,AnnouncementsView,Office_ShiftView,CountriesView,StateView
from .employees.views import Basic_EmployeeView,Bank_DetailsView,EmergencyView,SocialView,AttendanceView,LeaveView,DocumentsView
from .settings.views import Company_SettingView,Theme_SettingsView,LocalizationView,Email_SettingView,NotiView,LeavesView,SalaryView,Office_TimeView,RoleView
from rest_framework import routers

router = routers.DefaultRouter()
#----------------------------------------------------------------------
# Authendication
#----------------------------------------------------------------------
router.register('users',UsersView)
#----------------------------------------------------------------------
# Master
#----------------------------------------------------------------------
router.register('master-departments',DepartmentView)
router.register('master-designation',DesignationView)
router.register('master-blood',BloodView)
router.register('master-martial',MartialView)
router.register('master-gender',GenderView)
router.register('master-policies',PoliciesView)
router.register('master-anmouncement',AnnouncementsView)
router.register('master-office-shift',Office_ShiftView)
router.register('master-countries',CountriesView)
router.register('master-state',StateView)
#----------------------------------------------------------------------
# Employees
#----------------------------------------------------------------------
router.register('basic-employee',Basic_EmployeeView)
router.register('bank-details',Bank_DetailsView)
router.register('documents',DocumentsView)
router.register('emergency',EmergencyView)
router.register('social',SocialView)
router.register('attendance',AttendanceView)
router.register('leave',LeaveView)
#----------------------------------------------------------------------
# Settings
#----------------------------------------------------------------------
router.register('settings-company',Company_SettingView)
router.register('settings-theme',Theme_SettingsView)
router.register('settings-noti',NotiView)
router.register('settings-leave',LeavesView)
router.register('settings-role',RoleView)
router.register('settings-salary',SalaryView)
router.register('settings-localization',LocalizationView)
router.register('settings-email',Email_SettingView)
router.register('settings-office-time',Office_TimeView)


urlpatterns = [
    path('',include(router.urls),name='api')
]

urlpatterns += router.urls

