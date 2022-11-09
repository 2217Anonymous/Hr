from pyexpat import model
from django.db import models
from helpers import models as helpers
from master import models as master
from authentication import models as auth
from settings.models import Leaves
from django.contrib import messages
import datetime

# Create your models here.
class Basic_Employee(helpers.TrackingModel):
    user                = models.ForeignKey(auth.User,on_delete = models.CASCADE)
    DOB                 = models.DateField(null=True,help_text = "Please use the following format: <em>YYYY-MM-DD</em>.")
    Blood_Group         = models.ForeignKey(master.Blood,on_delete=models.PROTECT,null=True)
    Address_1           = models.CharField(max_length=100,null=True,help_text = "Float no,Street address.")
    Address_2           = models.CharField(max_length=100,null=True,help_text = "Apartment,Suite,Floor etc....")
    City                = models.CharField(max_length=30,null=True)
    Country             = models.ForeignKey(master.Countries,on_delete = models.PROTECT,null=True)
    State               = models.ForeignKey(master.State,on_delete = models.PROTECT,null=True)
    Postal_Code         = models.CharField(max_length=10,null=True)
    Martial_Status      = models.ForeignKey(master.Martial,on_delete = models.PROTECT,null=True)
    Religion            = models.CharField(max_length=20,null=True)
    Nationality         = models.CharField(max_length=15,null=True)
    Citizenship         = models.CharField(max_length=20,null=True)
    def __str__(self):
        return self.user.username

    @property
    def get_age(self):
        current_year = datetime.date.today().year
        dateofbirth_year = self.DOB.year
        if dateofbirth_year:
            return current_year - dateofbirth_year
        return

    @property
    def get_pretty_birthday(self):
        if self.DOB:
            return self.DOB.strftime('%A,%d %B') # Thursday,04 May -> staffs age privacy
        return

    @property
    def birthday_today(self):
        '''
        returns True, if birthday is today else False
        '''
        return self.DOB.day == datetime.date.today().day

    @property
    def days_check_date_fade(self):
        '''
        Check if Birthday has already been celebrated ie in the Past     ie. 4th May  & today 8th May 4 < 8 -> past else present or future '''
        return self.DOB.day < datetime.date.today().day #Assumption made,If that day is less than today day,in the past

    def birthday_counter(self):
        '''
        This method counts days to birthday -> 2 day's or 1 day
        '''
        today = datetime.date.today()
        current_year = today.year

        birthday = self.DOB # eg. 5th May 1995

        future_date_of_birth = datetime.date(current_year,birthday.month,birthday.day)#assuming born THIS YEAR ie. 5th May 2019

        if birthday:
            if (future_date_of_birth - today).days > 1:

                return str((future_date_of_birth - today).days) + ' day\'s'

            else:

                return ' tomorrow'

        return

class Emergency(helpers.TrackingModel):
    user                = models.ForeignKey(auth.User,on_delete = models.CASCADE)
    Emergency_Name      = models.CharField(max_length=30)
    Relationship        = models.CharField(max_length=30)
    Emergency_Phone     = models.CharField(max_length=15)
    Emergency_Email     = models.EmailField()
    Emergency_Address   = models.CharField(max_length=250)
    def __str__(self):
        return self.user.username

class Documents(helpers.TrackingModel):
    user          = models.ForeignKey(auth.User,on_delete = models.CASCADE)
    Document_Name = models.CharField(max_length=30)
    Document_Type = models.CharField(max_length=30)
    Document_File = models.FileField(upload_to='files/',default='default.pdf')
    def __str__(self):
        return self.user.username

class Social(helpers.TrackingModel):
    user            = models.ForeignKey(auth.User,on_delete = models.CASCADE)
    Name            = models.CharField(max_length=50)
    Profile_Url     = models.URLField(max_length=250)
    def __str__(self):
        return self.user.username
        
class Bank_Details(helpers.TrackingModel):
    user            = models.ForeignKey(auth.User,on_delete = models.CASCADE)
    Holder_Name     = models.CharField(max_length=20,null=True,blank=True)
    Account_No      = models.CharField(max_length=30,null=True,blank=True)
    Bank_Name       = models.CharField(max_length=30,null=True,blank=True)
    Branch_Location = models.CharField(max_length=150,null=True,blank=True)
    IFSC            = models.CharField(max_length=30,null=True,blank=True)
    PAN             = models.CharField(max_length=10,null=True,blank=True)
    Aadhar          = models.CharField(max_length=12,null=True,blank=True)
    def __str__(self):
        return self.user.username

class Attendance(helpers.Geolocation):
    user                = models.ForeignKey(auth.User,on_delete = models.CASCADE)
    Date                = models.DateField(auto_now_add=True)
    Manual_Dt           = models.DateField(null=True,blank=True)
    In_Time             = models.TimeField(null=True,blank=True)
    Out_Time            = models.TimeField(null=True,blank=True)
    Late_Time           = models.TimeField(null=True,blank=True)
    Early_Leaving       = models.TimeField(null=True,blank=True)
    Total_Working_Hours = models.TimeField(null=True,blank=True)
    Over_Time           = models.TimeField(null=True,blank=True)
    Clock_In            = models.BooleanField(default=False,null=True,blank=True)  
    Clock_Out           = models.BooleanField(default=False,null=True,blank=True)    
    Present             = models.BooleanField(default=False,null=True,blank=True)
    Absent              = models.BooleanField(default=False,null=True,blank=True)
    Half_Day            = models.BooleanField(default=False,null=True,blank=True)
    Late                = models.BooleanField(default=False,null=True,blank=True)
    Leave               = models.BooleanField(default=False,null=True,blank=True)
    Reason              = models.CharField(max_length=250,null=True,blank=True) 
    Status              = models.CharField(default='Absent',max_length=30,null=True,blank=True)

    def __str__(self):
        return self.user.username

    @property
    def getdate(self):
        date    = datetime(self.Date)
        return datetime.datetime.strptime(date,"%d")


class Leave(helpers.TrackingModel):
    user                    = models.ForeignKey(auth.User,on_delete=models.CASCADE)
    Start_Date              = models.DateField()
    End_Date                = models.DateField()
    Leave_Type              = models.ForeignKey(Leaves,on_delete=models.PROTECT)
    Reason                  = models.CharField(max_length=255,help_text='add additional information for leave',null=True,blank=True)
    Approved_Status         = models.CharField(max_length=12,default='pending',null=True,blank=True) #pending,approved,rejected,cancelled
    Approved_Description    = models.CharField(max_length=250,null=True,blank=True)
    is_approved             = models.BooleanField(default=False,null=True,blank=True) #hide

    def __str__(self):
        return self.user.username

    @property
    def leave_days(self):
        days_count  = ''
        start_dt    = self.Start_Date
        end_dt      = self.End_Date
        if start_dt > end_dt:
            return
        dates = (end_dt - start_dt)
        return dates.days
 

