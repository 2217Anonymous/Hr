from tokenize import PseudoExtras
from django.shortcuts import render,redirect
from django.contrib import messages
from settings import models
from settings import forms
from master import models as master_models
from django.contrib.auth.decorators import login_required,user_passes_test
from django.contrib.auth.models import User,Group,Permission
from authentication.models import Manager

# Create your views here.
#-------------------------------------------------------------------------------------------------------
@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def Settings(request):
    # perm = 0
    # perms = Permission.objects.filter(user=request.user)
    # for i in perms:
    #     if i.codename == "masteruser" : perm = 1
    # if perm == 0:
    #     error = "Access Denied"
    #     return render(request,'error.html',{'error':error})

    company      = models.Company_Setting.objects.all()
    theme        = models.Theme_Settings.objects.all()
    email        = models.Email_Setting.objects.all()
    salary       = models.Salary.objects.all()
    notification = models.Noti.objects.all()
    email        = models.Email_Setting.objects.all()
    country      = master_models.Countries.objects.all()
    state        = master_models.State.objects.all()

    context = {
        'company'   : company,
        'theme'     : theme,
        'email'     : email,
        'salary'    : salary,
        'noti'      : notification,
        'email'     : email,
        'country'   : country,
        'state'     : state,
        }
    return render(request,'settings/settings.html',context)

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def Company_settings(request):
    form    = forms.Company_Settings_Form()
    context = {'fm':form}
    if request.method == 'POST':
        form = forms.Company_Settings_Form(request.POST)
        if form.is_valid():
            models.Company_Setting.objects.all().delete()
            form.save()
            messages.success(request,'Form register successfully...!')
            return redirect('settings')
        else:
            messages.error(request,'Form is not valied...!')
            return redirect('settings')
    return render(request,'settings/settings.html',context)

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='/')
@user_passes_test(lambda user: user.is_admin)
def Theme(request,*args,**kwargs):
    form = forms.Theme_Settings_Form()
    if request.method == 'POST':
        form = forms.Theme_Settings_Form(request.POST,request.FILES)
        models.Theme_Settings.objects.all().delete()
        if form.is_valid():
            form.save()
            messages.success(request,'Theme is updated...!')
            return redirect('settings')
        else:
            messages.error(request,'Form is not valied...!')
            return redirect('settings')
    return render(request,"settings/settings.html",{'fm':form})

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='/')
@user_passes_test(lambda user: user.is_admin)
def Localization(request):
    form = forms.LocalizationForm()
    if request.method == 'POST':
        form = forms.LocalizationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings')
        else:
            messages.info(request,'Form is not valied...!')
            return redirect('settings')
    return render(request,"settings/settings.html",{'fm':form})

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='/')
@user_passes_test(lambda user: user.is_admin)
def Email_settings(request):
    form = forms.Email_Settings_Form()
    if request.method == 'POST':
        form = forms.Email_Settings_Form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Form is submitted...!')
            return redirect('settings')
        else:
            messages.error(request,'Form is not valied...!')
            return redirect('settings')
    return render(request,"settings/settings.html",{'fm':form})

@login_required(login_url='/')
@user_passes_test(lambda user: user.is_admin)
def Email_Edit(request):
    if request.method == 'POST':
        id   = request.POST.get('id')
        dt   = models.Email_Setting.objects.get(id=id)
        form = forms.Email_Settings_Form(request.POST,instance = dt)
        if form.is_valid():
            form.save()
            return redirect('settings')
        else:
            messages.info(request,'Form is not valid...!')
            return redirect('settings')
    return render(request,"Settings/settings.html",{'fm':form}) 

@login_required(login_url='/')
@user_passes_test(lambda user: user.is_admin)
def Email_Delete(request, id):  
    email = models.Email_Setting.objects.get(id=id)  
    email.delete()  
    messages.success(request,'Email setting deleted...!')
    return redirect("settings")

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='/')
@user_passes_test(lambda user: user.is_admin)
def Notification(request):
    form = forms.Notiform()
    if request.method == 'POST':
        form = forms.Notiform(request.POST)
        if form.is_valid():
            models.Noti.objects.all().delete()
            form.save()
            messages.success(request,'Notification Set...!')
            return redirect('settings')
        else:
            messages.error(request,'Form is not valied...!')
            return redirect('settings')
    return render(request,"Settings/settings.html",{'fm':form})

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='/')
@user_passes_test(lambda user: user.is_admin)
def Leave(request):
    data=models.Leaves.objects.all()
    form = forms.Lform()
    if request.method == 'POST':
        form = forms.Lform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('settings')
        else:
            messages.info(request,'Form is not valied...!')
            return redirect('settings')
    return render(request,"settings/leave.html",{'fm':form,'data':data})

@login_required(login_url='/')
@user_passes_test(lambda user: user.is_admin)
def Leave_Edit(request, id):  
    data = models.Leaves.objects.all()  
    if request.method == 'POST':
        id   = request.POST.get('id')
        dt   = models.Leaves.objects.get(id=id)
        form = forms.Lform(request.POST,instance = dt)
        if form.is_valid():
            form.save()
            return redirect('settings')
        else:
            messages.info(request,'Form is not valid...!')
            return redirect('settings')
    return render(request,"settings/settings.html",{'data':data})

@login_required(login_url='/')
@user_passes_test(lambda user: user.is_admin)
def Leave_Delete(request, id):  
    leave = models.Leaves.objects.get(id=id)  
    leave.delete()  
    return redirect("/settings/")

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='/')
@user_passes_test(lambda user: user.is_admin)
def Permission(request):
    form = forms.Roleform()
    if request.method == 'POST':
        form = forms.Roleform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Permission Updated...!')
            return redirect('settings')
        else:
            messages.error(request,'Form is not valied...!')
            return redirect('settings')
    return render(request,"settings/settings.html",{'fm':form})

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='/')
@user_passes_test(lambda user: user.is_admin)
def Salary_Settings(request):
    form = forms.Salaryform()
    if request.method == 'POST':
        form = forms.Salaryform(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Salary settings added...!')
            return redirect('settings')
        else:
            messages.info(request,'Form is not valied...!')
            return redirect('settings')
    return render(request,'settings/settings.html')

#-------------------------------------------------------------------------------------------------------
