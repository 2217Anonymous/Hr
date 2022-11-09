from django.db import models
from helpers import models as helpers
from master import models as master

Country= [
    ('India', 'India'),
    ('Pakistan', 'Pakistan'),
    ('Srilanga', 'Srilanga'),
    ('Austrlia', 'Austrlia'),
    ]
State= [
    ('Tamilnadu', 'Tamilnadu'),
    ('Kerala', 'Kerala'),
    ('Karnataka', 'Karnataka'),
    ('Delhi', 'Delhi'),
    ]
City= [
    ('Tirupur', 'Tirupur'),
    ('Madurai', 'Madurai'),
    ('Coimbatore', 'Coimbatore'),
    ('Chennai', 'Chennai'),
    ]

Date_Format= [
    ('15/05/2016', '15/05/2016'),
    ('15.05.2016', '15.05.2016'),
    ('15-05-2016', '15-05-2016'),
    ('05/15/2016', '05/15/2016'),
    ('2016/05/15', '2016/05/15'),
    ('2016-05-15', '2016-05-15'),
    ('15 May 2016', '15 May 2016'),
    ('May 15 2016', 'May 15 2016'),
    ]

Timezone = [
    ('(UTC +5:30) Antarctica/Palmer', '(UTC +5:30) Antarctica/Palmer'),
    ]

Language = [
    ('Tamil', 'Tamil'),
    ('English', 'English'),
    ('French', 'French'),
    ]

Currency_Code = [
    ('INR','INR'),
    ('USD', 'USD'),
    ('Pound', 'Pound'),
    ('EURO', 'EURO'),
    ]
Security = [
    ('None','None'),
    ('SSL', 'SSL'),
    ('TLS', 'TLS'),
    ]
status = [
    ('active', 'active'),
    ('deactive', 'deactive'),
]
role = [
    ('Administrator', 'Administrator'),
    ('CEO', 'CEO'),
    ('Manager', 'Manager'),
    ('Team Leader', 'Team Leader'),
    ('Accountant', 'Accountant'),
    ('Web Developer', 'Web Developer'),
    ('Web Designer', 'Web Designer'),
    ('HR', 'HR'),
    ('UI/UX Developer', 'UI/UX Developer'),
    ('SEO Analyst', 'SEO Analyst'),
]

class Company_Setting(helpers.TrackingModel):
    Company_Name    = models.CharField(max_length=50,error_messages ={"max_length":"Maximum Char 50!."})
    Contact_Person  = models.CharField(max_length=50,error_messages ={"max_length":"Maximum Char 50!."})
    Address         = models.CharField(max_length=100)
    Country         = models.ForeignKey(master.Countries,on_delete = models.PROTECT,null=True)
    State           = models.ForeignKey(master.State,on_delete = models.PROTECT,null=True)
    Postal_Code     = models.IntegerField()
    Email           = models.EmailField(max_length=70,unique=True,error_messages ={"unique":"The Email Field already used."})
    Phone_Number    = models.CharField(max_length=10)
    Website_URL     = models.URLField(max_length=200)
    def __str__(self):
        return self.Company_Name

class Theme_Settings(helpers.TrackingModel):
    Web_Name        = models.CharField(max_length=50, error_messages={"max_length": 'Maximum Length is 50!'})
    Logo            = models.ImageField(upload_to="picture/")
    Favicon         = models.ImageField(upload_to="picture/")
    Login           = models.ImageField(upload_to="picture/")
    def __str__(self):
        return self.Web_Name

class Localization(helpers.TrackingModel):
    Country         = models.ForeignKey(master.Countries,on_delete = models.PROTECT,null=True)
    Date_Format     = models.CharField(max_length=30,choices=Date_Format, default='Select')
    Timezone        = models.CharField(max_length=30,choices=Timezone, default='Select')
    Language        = models.CharField(max_length=30,choices=Language, default='Select')
    Currency_Code   = models.CharField(max_length=30,choices=Currency_Code, default='Select')
    Currency_Symbol = models.CharField(max_length=30,default='$')
    def __str__(self):
        return self.Country

class Email_Setting(helpers.TrackingModel):
    Name            = models.CharField(max_length=30, error_messages={"max_length": 'Maximum Length is 30!'})
    Sender_Email    = models.CharField(max_length=30, error_messages={"max_length": 'Maximum Length is 30!'})
    Sender_Name     = models.CharField(max_length=30, error_messages={"max_length": 'Maximum Length is 30!'})
    SMTP_Host       = models.CharField(max_length=30, error_messages={"max_length": 'Maximum Length is 30!'})
    SMTP_User       = models.CharField(max_length=30, error_messages={"max_length": 'Maximum Length is 30!'})
    SMTP_Password   = models.CharField(max_length=30, error_messages={"max_length": 'Maximum Length is 30!'})
    SMTP_Port       = models.IntegerField()
    Default_Server  = models.CharField(max_length=30, error_messages={"max_length": 'Maximum Length is 30!'})
    def __str__(self):
        return self.SMTP_Host

class Noti(helpers.TrackingModel):
    Employee    = models.BooleanField(error_messages={'required': 'Please Grant the Permission'})
    Holidays    = models.BooleanField(error_messages={'required': 'Please Grant the Permission'})
    Leaves      = models.BooleanField(error_messages={'required': 'Please Grant the Permission'})
    Events      = models.BooleanField(error_messages={'required': 'Please Grant the Permission'})
    Chat        = models.BooleanField(error_messages={'required': 'Please Grant the Permission'})
    Jobs        = models.BooleanField(error_messages={'required': 'Please Grant the Permission'})

class Leaves(helpers.TrackingModel):
    Leave   = models.CharField(max_length=30)
    Days    = models.IntegerField()
    def __str__(self):
        return self.Leave

class Role (helpers.TrackingModel):
    Roles           = models.CharField(max_length=30, choices=role, default='Select')
    Grant_Employee  = models.BooleanField()
    Em_Create       = models.BooleanField()
    Em_Write        = models.BooleanField()
    Em_Read         = models.BooleanField()
    Em_Delete       = models.BooleanField()
    Grant_Holidays  = models.BooleanField()
    H_Create        = models.BooleanField()
    H_Write         = models.BooleanField()
    H_Read          = models.BooleanField()
    H_Delete        = models.BooleanField()
    Grant_Leaves    = models.BooleanField()
    L_Create        = models.BooleanField()
    L_Write         = models.BooleanField()
    L_Read          = models.BooleanField()
    L_Delete        = models.BooleanField()
    Grant_Events    = models.BooleanField()
    E_Create        = models.BooleanField()
    E_Write         = models.BooleanField()
    E_Read          = models.BooleanField()
    E_Delete        = models.BooleanField()
    Grant_Chat      = models.BooleanField()
    C_Create        = models.BooleanField()
    C_Write         = models.BooleanField()
    C_Read          = models.BooleanField()
    C_Delete        = models.BooleanField()
    Grant_Jobs      = models.BooleanField()
    J_Create        = models.BooleanField()
    J_Write         = models.BooleanField()
    J_Read          = models.BooleanField()
    J_Delete        = models.BooleanField()
    def __str__(self):
        return self.Roles

class Salary(helpers.TrackingModel):
    DA_HRA      = models.BooleanField()
    DA          = models.IntegerField(blank=True, null=True)
    HRA         = models.IntegerField(blank=True,null=True)
    PF          = models.BooleanField()
    Emp_Share   = models.IntegerField(blank=True,null=True)
    Org_Share   = models.IntegerField(blank=True,null=True)
    ESI         = models.BooleanField()
    E_Share     = models.IntegerField(blank=True,null=True)
    O_Share     = models.IntegerField(blank=True,null=True)

class Office_Time(helpers.TrackingModel):
    In  = models.TimeField()
    Out = models.TimeField()