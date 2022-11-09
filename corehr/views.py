from django.shortcuts import render,redirect
from settings.models import Theme_Settings

def index(request):
    logo = Theme_Settings.objects.all()
    context = {
        'logo' : logo
    }
    return render(request,"index.html",context)