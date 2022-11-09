from rest_framework import serializers
from settings import models

class Company_SettingSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Company_Setting
        fields = '__all__'

class Theme_SettingsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Theme_Settings
        fields = '__all__'

class LocalizationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Localization
        fields = '__all__'

class Email_SettingSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Email_Setting
        fields = '__all__'

class NotiSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Noti
        fields = '__all__'

class LeaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Leaves
        fields = '__all__'

class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'

class SalarySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Salary
        fields = '__all__'

class Office_TimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Office_Time
        fields = '__all__'
