from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.employees.serializers import Basic_EmployeeSerializers,EmergencySerializers,DocumentsSerializers,SocialSerializers,Bank_DetailsSerializers,AttendanceSerializers,LeaveSerializers
from employees import models

class Basic_EmployeeView(ModelViewSet):
    queryset = models.Basic_Employee.objects.all()
    serializer_class = Basic_EmployeeSerializers

class EmergencyView(ModelViewSet):
    queryset = models.Emergency.objects.all()
    serializer_class = EmergencySerializers

class DocumentsView(ModelViewSet):
    queryset = models.Documents.objects.all()
    serializer_class = DocumentsSerializers

class SocialView(ModelViewSet):
    queryset = models.Social.objects.all()
    serializer_class = SocialSerializers

class Bank_DetailsView(ModelViewSet):
    queryset = models.Bank_Details.objects.all()
    serializer_class = Bank_DetailsSerializers

class AttendanceView(ModelViewSet):
    queryset = models.Attendance.objects.all()
    serializer_class = AttendanceSerializers

class LeaveView(ModelViewSet):
    queryset = models.Leave.objects.all()
    serializer_class = LeaveSerializers