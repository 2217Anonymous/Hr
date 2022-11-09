from rest_framework.response import Response
from rest_framework.decorators import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from api.master.serializers import DepartmentSerializers,DesignationSerializers,CountriSerializers,StateSerializers,BloodSerializers,MartialSerializers,GenderSerializers,PolicieSerializers,AnnouncementsSerializers,Office_ShiftSerializers
from master import models

class DepartmentView(ModelViewSet):
    queryset = models.Departments.objects.all()
    serializer_class = DepartmentSerializers

class DesignationView(ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = DesignationSerializers

class CountriesView(ModelViewSet):
    queryset = models.Countries.objects.all()
    serializer_class = CountriSerializers

class StateView(ModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = StateSerializers

class BloodView(ModelViewSet):
    queryset = models.Blood.objects.all()
    serializer_class = BloodSerializers

class MartialView(ModelViewSet):
    queryset = models.Martial.objects.all()
    serializer_class = MartialSerializers

class GenderView(ModelViewSet):
    queryset = models.Gender.objects.all()
    serializer_class = GenderSerializers

class PoliciesView(ModelViewSet):
    queryset = models.Policies.objects.all()
    serializer_class = PolicieSerializers

class AnnouncementsView(ModelViewSet):
    queryset = models.Announcements.objects.all()
    serializer_class = AnnouncementsSerializers

class Office_ShiftView(ModelViewSet):
    queryset = models.Office_Shift.objects.all()
    serializer_class = Office_ShiftSerializers