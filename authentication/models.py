from django.db import models
from django.contrib.auth.models import AbstractUser
from master import models as master
# Create your models here.

COLOR_CHOICES = (
    ('night','NIGHT'),
    ('morning', 'MORNING'),
)

class User(AbstractUser):
    Employee_Id     = models.IntegerField(unique=True,null=True,blank=True)
    Phone           = models.CharField(max_length=15,null=True,unique = True)
    Gender          = models.ForeignKey(master.Gender,on_delete=models.PROTECT,null=True)
    Profile_Pic     = models.ImageField(upload_to='profile/',default='profile/profile.png')
    Department      = models.ForeignKey(master.Departments,on_delete=models.PROTECT,null=True)
    Designation     = models.ForeignKey(master.Designation,on_delete=models.PROTECT,null=True)
    Date_Of_Joining = models.DateField(null=True,blank=True)
    Resignation_Dt  = models.DateField(null=True,blank=True)
    Termination_Dt  = models.DateField(null=True,blank=True)
    Shift_Type      = models.ForeignKey(master.Office_Shift,on_delete=models.PROTECT,null=True)
    Salary          = models.IntegerField(null=True,blank=True) 
    is_employee     = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    is_client       = models.BooleanField(default=False)
    auth_token      = models.CharField(max_length=100,null=True )
    is_verified     = models.BooleanField(default=False,null=True)
    def __str__(self):
        return self.username

class Manager(models.Model):
    Profile_Pic = models.ImageField(upload_to='manager/',default='profile/profile.png')
    name        = models.CharField(max_length=30)
    utext       = models.TextField()
    email       = models.CharField(max_length=250)
    def __str__(self):
        return self.name

