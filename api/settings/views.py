from rest_framework.viewsets import ModelViewSet
from api.settings.serializers import Company_SettingSerializers,Theme_SettingsSerializers,LocalizationSerializers,Email_SettingSerializers,NotiSerializers,LeaveSerializers,RoleSerializers,SalarySerializers,Office_TimeSerializers
from settings import models

class Company_SettingView(ModelViewSet):
    queryset = models.Company_Setting.objects.all()
    serializer_class = Company_SettingSerializers

class Theme_SettingsView(ModelViewSet):
    queryset = models.Theme_Settings.objects.all()
    serializer_class = Theme_SettingsSerializers

class LocalizationView(ModelViewSet):
    queryset = models.Localization.objects.all()
    serializer_class = LocalizationSerializers

class Email_SettingView(ModelViewSet):
    queryset = models.Email_Setting.objects.all()
    serializer_class = Email_SettingSerializers

class NotiView(ModelViewSet):
    queryset = models.Noti.objects.all()
    serializer_class = NotiSerializers

class LeavesView(ModelViewSet):
    queryset = models.Leaves.objects.all()
    serializer_class = LeaveSerializers

class RoleView(ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = RoleSerializers

class SalaryView(ModelViewSet):
    queryset = models.Salary.objects.all()
    serializer_class = SalarySerializers

class Office_TimeView(ModelViewSet):
    queryset = models.Office_Time.objects.all()
    serializer_class = Office_TimeSerializers

