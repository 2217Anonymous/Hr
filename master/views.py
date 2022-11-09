from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from master import models
from master import forms
from authentication.models import User
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
#----------------------START DEPARTMENT----------------------------------------
@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def Department(request):
    dt_Dept     = models.Departments.objects.all().order_by('-id')
    form        = forms.Department_Form()
    if request.method == 'POST':
        pdict = request.POST.copy()
        form = forms.Department_Form(pdict)
        if form.is_valid():
            form.save()
            messages.success(request,'Department added Successfully...!')
            return redirect('department')
        else:
            form = forms.Department_Form(request.POST)
            messages.error(request,'Form is not valid...!') 
    context     = { 'fm': form,'tbl_data' : dt_Dept}
    return render(request,"master/department.html",context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def Dept_Edit(request):
    if request.method == 'POST':
        id   = request.POST.get('id')
        dt   = models.Departments.objects.get(id=id)
        form = forms.Department_Form(request.POST,instance = dt)
        if form.is_valid():
            form.save()
            return redirect('department')
        else:
            messages.error(request,'Form is not valid...!')
            return redirect('department')
    return render(request,"master/department.html")

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def Dept_Delete(request,id):
    try:
        Department = models.Departments.objects.get(id=id);
        Department.delete()
        messages.success(request,'Department deleted Successfully...!')
        return redirect("/master/department/")
    except Exception as e:
        messages.error(request,e)
        return redirect("/master/department/")

#----------------------END DEPARTMENT----------------------------------------
#----------------------START DESIGNATION--------------------------------------
@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def Designation(request):
    dt              = models.Departments.objects.filter(status=True)
    dt_Designation  = models.Designation.objects.all().order_by("-id")
    form            = forms.Designation_Form()
    context = {
        'drop_data' : dt,
        'tbl_data'  : dt_Designation,
        'fm'        : form, 
    }
    if request.method == 'POST':
        pdict   = request.POST.copy()
        form    = forms.Designation_Form(pdict)
        if form.is_valid():
            form.save()
            messages.success(request,'Department added Successfully...!')
            return redirect('designation')
        else:
            form = forms.Designation_Form(request.POST)
            messages.error(request,'Form is not valid...!')
    return render(request,'master/designation.html',context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def Designation_Edit(request):
    dt      = models.Departments.objects.filter(status=True)
    context = {
        'drop_data' : dt,
    }
    if request.method == 'POST':
        id   = request.POST.get("id")
        dt   = models.Designation.objects.get(id=id)
        form = forms.Designation_Form(request.POST,instance = dt)
        if form.is_valid():
            form.save()
            return redirect('designation')
        else:
            messages.info(request,'Form is not valid...!')
            return redirect('des_edit/<int:id>')
    return render(request,"master/designation.html",context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def Designation_Delete(request,id):
    Designation = models.Designation.objects.get(id=id);
    Designation.delete()
    return redirect("/master/designation/")

#----------------------END DESIGNATION----------------------------------------