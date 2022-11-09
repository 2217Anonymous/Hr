from django.db import models
import socket    
from django.contrib import admin
from datetime import datetime,time,timedelta
hostname   = socket.gethostname()    
IP         = socket.gethostbyname(hostname) 

class TrackingModel(models.Model):
    status      = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now = True)
    class Meta:
        abstract    = True
        ordering    = ('-created_at',)

class Geolocation(models.Model):
    ipaddress   = models.GenericIPAddressField()
    latitude    = models.CharField(max_length=50,null=True,blank=True)
    longitude   = models.CharField(max_length=50,null=True,blank=True)
    class Meta:
        abstract    = True

class Trackadmin(admin.ModelAdmin): 
    list_display    = [
        'status',
        'created_at',
        'updated_at',
     ]


def datetime_convert(date_time):
    dt_      = date_time
    time_    = dt_.strftime('%H : %M : %S.%f')
    get_time = datetime.strptime(time_,'%H : %M : %S.%f')
    return get_time

def time_convert(date_time):
    format          = '%I:%M%p'
    datetime_str    = datetime.strptime(date_time, format)
    return datetime_str

class time_calculator:
    def add_time():
        pass
    
    def sub_time(time1,time2):
        get_time = timedelta(
                hours   = (time1.hour    - time2.hour),
                minutes = (time1.minute  - time2.minute),
            )
        return str(get_time)

    def time_difference(time1,time2):
        get_difference = time1 - time2
        return str(get_difference)

    def daterange(start_date, end_date):
        for n in range(int ((end_date - start_date).days)):
            yield start_date + timedelta(n)
