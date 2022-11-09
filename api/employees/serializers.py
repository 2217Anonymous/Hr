from rest_framework import serializers
from employees import models
#from api.helperserializers import TrackingModelSerializers

class Basic_EmployeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Basic_Employee
        fields = '__all__'

class EmergencySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Emergency
        fields = '__all__'

class DocumentsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Documents
        fields = '__all__'

class SocialSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Social
        fields = '__all__'

class Bank_DetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Bank_Details
        fields = '__all__'

class AttendanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Attendance
        fields = '__all__'

class LeaveSerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Leave
        fields = '__all__'