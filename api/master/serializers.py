from rest_framework import serializers
from master import models

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Departments
        fields = '__all__'

class DesignationSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Designation
        fields = "__all__"

class CountriSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Countries
        fields = "__all__"

class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = "__all__"

class BloodSerializers(serializers.ModelSerializer):
    class Meta:
        model  = models.Blood
        fields = "__all__"

class MartialSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Martial
        fields = "__all__"

class GenderSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Gender
        fields = "__all__"

class PolicieSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Policies
        fields = "__all__"

class AnnouncementsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Announcements
        fields = "__all__"

class Office_ShiftSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Announcements
        fields = "__all__"