from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from settings import models
# Create your views here.
@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def Dashboard(request):
    return render(request,'admin/hr-dashboard.html')

def Side_Bar(request):
    Logo = models.Theme_Settings.objects.all()
    context = {
        'img' : Logo
    }
    return render(request,'admin/hr-dashboard',context)
