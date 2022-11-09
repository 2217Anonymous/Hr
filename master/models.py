from django.db import models
from helpers.models import TrackingModel

# Create your models here.
class Departments(TrackingModel):
    Department_Name = models.CharField(max_length=30)
    Department_Head = models.CharField(max_length=30)
    def __str__(self):
        return self.Department_Name
    
class Designation(TrackingModel):
    Department_Name = models.ForeignKey(Departments,on_delete=models.PROTECT)
    Designation     = models.CharField(null=False,max_length=50,unique=True)
    Description     = models.CharField(null=False,max_length=50)
    def __str__(self):
        return self.Designation

class Countries(models.Model):
    Sort_Name       = models.CharField(max_length=50)
    Country_Name    = models.CharField(max_length=150)
    Phone_Code      = models.CharField(max_length=10)
    def __str__(self):
        return self.Country_Name

class State(models.Model):
    Country_Name    = models.ForeignKey(Countries, on_delete=models.CASCADE)
    State_Name      = models.CharField(max_length=150)
    def __str__(self):
        return self.State_Name

class Blood(TrackingModel):
    Blood_Group     = models.CharField(max_length=20)
    def __str__(self):
        return self.Blood_Group

class Gender(TrackingModel):
    Gender          = models.CharField(max_length=10)
    def __str__(self):
        return self.Gender

class Martial(TrackingModel):
    Martial         = models.CharField(max_length=20)
    def __str__(self):
        return self.Martial 

class Policies(TrackingModel):
    Title           = models.CharField(max_length=50)
    Description     = models.TextField()
    Attachement     = models.FileField(upload_to="policie_files/")
    def __str__(self):
        return self.Title

class Announcements(TrackingModel):
    Title           = models.CharField(max_length=50)
    Department      = models.ForeignKey(Departments,on_delete=models.PROTECT)
    Start_Date      = models.DateField()
    End_Date        = models.DateField()
    Summery         = models.TextField()
    Description     = models.TextField()
    def __str__(self):
        return self.Title

class Office_Shift(TrackingModel):
    Shift_Type  = models.CharField(max_length=30)
    Start_Time  = models.TimeField()
    End_Time    = models.TimeField() 
    def __str__(self):
        return self.Shift_Type