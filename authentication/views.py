from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import auth,Group,Permission
from django.contrib.contenttypes.models import ContentType
from django.conf import settings
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from master import models as master
from django.contrib import messages
from authentication import models as authmodel
from settings.models import Theme_Settings
from django.db.models import Max
from authentication import forms
from authentication import models as authentication
from django.contrib.auth.decorators import login_required,user_passes_test
import uuid
from django.conf import settings
from django.core.mail import send_mail
from .models import Manager

#-------------------------------------------------------------------------------------------------------

def check(request):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})
# Create your views here.
#User = settings.AUTH_USER_MODEL

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def employee_register(request):
    e           = authmodel.User.objects.aggregate(Max('Employee_Id'))
    EmpId       = 1001 if authmodel.User.objects.count() == 0 else authmodel.User.objects.aggregate(max=Max('Employee_Id'))["max"]+1
    dt_User     = authmodel.User.objects.all()
    Gender      = master.Gender.objects.filter(status=True)
    Dept        = master.Departments.objects.filter(status=True)
    Desg        = master.Designation.objects.filter(status=True)
    Shift       = master.Office_Shift.objects.filter(status=True)
    emp_form    = forms.Employee_RegisterForm()
    context = {
        'tbl_data'      : dt_User,
        'Gender_data'   : Gender,
        'Dept_data'     : Dept,
        'Desg_data'     : Desg,
        'emp_form'      : emp_form,
        'emp_id'        : EmpId,
        'Shift_data'    : Shift,
    }
    if request.method == 'POST':
        emp_id          = request.POST.get('Employee_Id')
        profile_pic     = request.FILES.get('Profile_Pic')
        username        = request.POST.get('username')
        pass1           = request.POST.get('password1')
        pass2           = request.POST.get('password2')
        firstname       = request.POST.get('first_name')
        lastname        = request.POST.get('last_name')
        email           = request.POST.get('email')
        phone           = request.POST.get('Phone')
        gender          = request.POST.get('Gender')
        department      = request.POST.get('Department')
        designation     = request.POST.get('Designation')
        doj             = request.POST.get('Date_Of_Joining')
        shift_type      = request.POST.get('Shift_Type')
        salary          = request.POST.get('Salary')
        isemployee      = request.POST.get('is_employee')
        isadmin         = request.POST.get('is_admin')
        isclient        = request.POST.get('is_client')
        #try:
            # if not emp_id:
            #     messages.error(request,'Employee Id is required!')
            # if not username:
            #     messages.error(request,'username is required!')
            # if authentication.User.objects.filter(username=username).exists():
            #     messages.error(request,'Username is taken, choose another one')
            # if len(pass1) < 6:
            #         messages.error(request,'Password should be at least 6 characters!')
            # if pass1==pass2:
            #         messages.error(request,'Password mismatch!')
            # if not doj:
            #     messages.error(request,"Date of join is must")
            # if authentication.User.objects.filter(email=email).exists():
            #         messages.error(request,'Mail id is taken, choose another one')
            # if not isemployee or not isadmin or not isclient:
            #     messages.error(request,'employee or admin or client are any one required!')
        if isemployee == 'on':
            isemployee = True
        else:
            isemployee = False
        if isadmin == 'on':
            isadmin = True
        else:
            isadmin = False
        if isclient == 'on':
            isclient = True
        else:
            isclient = False

        auth_token = str(uuid.uuid4())

        user = authentication.User.objects.create(
                    Employee_Id     = emp_id,
                    Profile_Pic     = profile_pic,
                    username        = username,
                    first_name      = firstname,
                    last_name       = lastname,
                    email           = email,
                    Phone           = phone,
                    Gender          = 'Male' if gender == '1' else ('Female' if gender == '2' else 'Others'),
                    Department_id   = department,
                    Designation_id  = designation,
                    Date_Of_Joining = doj,
                    Shift_Type      = shift_type,
                    Salary          = salary,
                    is_employee     = isemployee,
                    is_admin        = isadmin,
                    is_client       = isclient,
                    auth_token      = auth_token
                )
        user.set_password(pass1)
        user.save()
        manager = Manager.objects.create(Profile_Pic=profile_pic,name = firstname + lastname,utext = username,email = email)
        manager.save()
        send_mail_after_registration(email , auth_token)
        messages.success(request,'User Register Successfull!')
        return redirect('employee-details')
        # except Exception as e:
        #     messages.error(request,e)
    return render(request,'employee/employee-register.html',context)

def edit_employee(request,id,token,name):
    emp_data = authmodel.User.objects.filter(auth_token=token,id=id,first_name=name)
    Dept     = master.Departments.objects.filter(status=True)
    Desg     = master.Designation.objects.filter(status=True)
    Shift    = master.Office_Shift.objects.filter(status=True)
    Gender   = master.Gender.objects.filter(status=True)
    context  = {
        'data'      : emp_data,
        'Dept_data' : Dept,
        'Desg_data' : Desg,
        'Gender'    : Gender,
        'Shift'     : Shift,
    }
    if request.method == "POST":
        firstname       = request.POST.get('first_name')
        lastname        = request.POST.get('last_name') 
        email           = request.POST.get('email')
        phone           = request.POST.get('Phone')
        gender          = request.POST.get('Gender')
        department      = request.POST.get('Department')
        designation     = request.POST.get('Designation')
        doj             = request.POST.get('Date_Of_Joining')
        shift_type      = request.POST.get('Shift_Type')
        salary          = request.POST.get('Salary')
        isemployee      = request.POST.get('is_employee')
        isadmin         = request.POST.get('is_admin')
        isclient        = request.POST.get('is_client')

        authmodel.User.objects.filter(pk=id,auth_token=token,first_name=name).update(
            first_name      = firstname,
            last_name       = lastname,
            email           = email,
            Phone           = phone,
            Gender          = 'Male' if gender == '1' else ('Female' if gender == '2' else 'Others'),
            Department_id   = department,
            Designation_id  = designation,
            Date_Of_Joining = doj,
            Shift_Type      = shift_type,
            Salary          = salary,
            is_employee     = True if isemployee == 'on' else False,
            is_admin        = True if isadmin == 'on' else False,
            is_client       = True if isclient == 'on' else False,
        )
        messages.success(request,'updated successfully...!')
        return redirect('employee-list')
    return render(request,'employee/edit-employee.html',context)

def update_profile(request,id,token,name):
    if request.method == "POST":
        profile_pic     = request.FILES.get('Profile_Pic')        
        authmodel.User.objects.filter(pk=id,auth_token=token,first_name=name).update(
            Profile_Pic = profile_pic,
        )
        messages.success(request,'updated successfully...!')
    return redirect('employee-details')

#-------------------------------------------------------------------------------------------------------

def verify(request , auth_token):
    try:
        token = authentication.User.objects.filter(auth_token = auth_token).first()
        if token:
            if token.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('login')
            token.is_verified = True
            token.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('login')
        else:
            messages.error(request,"Your not verified please check your mail")
            return redirect('login')
    except Exception as e:
        print(e)
        return redirect('login')

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def user_delete(request,pk):
    user = authentication.User.objects.get(id=pk)
    user.delete()
    messages.success(request,'User deleted Successfully...!')
    return redirect('employee-register')

#-------------------------------------------------------------------------------------------------------

def login(request):
    logo = Theme_Settings.objects.all();
    context = {
        'login' : logo,
    }
    if request.method == 'POST':
        username = request.POST.get('username')#venkat
        password = request.POST.get('password')#snvnkdbvkb

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            if user.is_admin and user.is_active:
                if user.is_verified:
                    auth.login(request,user)
                    if request.GET.get('next'):
                        messages.warning(request,'“Sorry, You Are Not Allowed to Access This Page”')
                        return redirect(request.GET.get('next'))
                    else:
                        messages.success(request,' Welcome {0}'.format(username))
                        return redirect("/hr-dashboard/")
                else:
                    messages.error(request,"Email is not verfied!")

            elif user.is_employee and user.is_active:
                if user.is_verified:
                    auth.login(request,user)
                    if request.GET.get('next'):
                        messages.warning(request,'“Sorry, You Are Not Allowed to Access This Page”')
                        return redirect(request.GET.get('next'))
                    else:
                        messages.success(request,'Welcome {0}'.format(username))
                        return redirect("/employee/")
                else:
                    messages.error(request,"Email is not verfied!")
        else:
            messages.error(request,"Invalid credentials, try again")
    return render(request,'auth/login.html',context)

#-------------------------------------------------------------------------------------------------------

def logout(request):
    auth.logout(request)
    return('login')

#-------------------------------------------------------------------------------------------------------

def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject,
        message , 
        email_from ,
        ['venkateshwaran.sort@gmail.com'],
        fail_silently=False 
    ) 

#-------------------------------------------------------------------------------------------------------

def manager_list(request):
    perm = 0
    group = request.user.groups.all()
    print('------------------------------')
    print(group)
    print('------------------------------')
    for i in request.user.groups.all():
        if i.name == 'Master_admin': 
            perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})
    manager = Manager.objects.all()
    return render(request,'auth/manager-list.html',{'manager':manager})

def manager_del(request,pk):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})
    manager = Manager.objects.get(pk=pk)
    _del    = authmodel.User.objects.filter(username = manager.utext)
    _del.delete()
    manager.delete()
    return redirect('manager-list')

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def groups(request):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})
    group = Group.objects.all().exclude(name="Master_admin")
    return render(request,'auth/group.html',{'group':group})

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def group_add(request):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})

    if request.method == "POST":
        name = request.POST.get('name')
        if name != "":
            if len(Group.objects.filter(name=name)) == 0:
                group = Group(name=name)
                group.save()
    return redirect(groups)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def group_del(request,name):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})
    _del = Group.objects.filter(name=name)
    _del.delete()
    return redirect(groups)

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def user_group(request,pk):
    manager = Manager.objects.get(pk=pk)
    user    = authmodel.User.objects.get(username=manager.utext)
    ugroup   = []
    for i in user.groups.all():
        ugroup.append(i.name)

    group = Group.objects.all()
    context = {
        'ugroup':   ugroup,
        'group' :   group,
        'pk'    :   pk,
    }
    return render(request,'auth/user-group.html',context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def add_user_group(request,pk):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})

    if request.method=="POST":
        gname = request.POST.get('gname')

        group       = Group.objects.get(name=gname)
        manager     = authmodel.Manager.objects.get(pk=pk)
        user        = authmodel.User.objects.get(username=manager.utext)
        user.groups.add(group)
    return redirect('user-group',pk)

def del_user_group(request,pk,name):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})

    group       = Group.objects.get(name=name)
    manager     = authmodel.Manager.objects.get(pk=pk)
    user        = authmodel.User.objects.get(username=manager.utext)
    user.groups.remove(group)
    return redirect('user-group',pk)

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def perms(request):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})
    perms = Permission.objects.all()
    return render(request,'auth/permission.html',{'perms':perms})

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def perms_del(request,name):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})

    perms = Permission.objects.filter(name=name)
    perms.delete()
    return HttpResponseRedirect('/accounts/perms/')

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def perms_add(request):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})

    if request.method == "POST":
        name    = request.POST.get('name')
        cname   = request.POST.get('cname') 

        if len(Permission.objects.filter(codename=cname)) == 0:
            content_type    = ContentType.objects.get(app_label='authentication',model='user')
            permission      = Permission.objects.create(codename=cname,name=name,content_type=content_type)
        else:
            messages.error(request,'This codename used before...!')
    return redirect('perms')

#-------------------------------------------------------------------------------------------------------

def user_perms(request,pk):
    manager     = Manager.objects.get(pk=pk)
    user        = authmodel.User.objects.get(username=manager.utext)
    permission  = Permission.objects.filter(user=user)

    uperms = []
    for i in permission:
        uperms.append(i.name)

    perms = Permission.objects.all()
    context = {
        'uperms':   uperms,
        'perms' :   perms,
        'pk'    :   pk,
    }
    return render(request,'auth/user-permission.html',context)


@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def add_user_perms(request,pk):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})

    if request.method=="POST":
        pname = request.POST.get('pname')

        manager     = authmodel.Manager.objects.get(pk=pk)
        user        = authmodel.User.objects.get(username=manager.utext)
        permission  = Permission.objects.get(name=pname)
        user.user_permissions.add(permission)
    return redirect('user-perms',pk)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def del_user_perms(request,pk,name):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})

    manager = Manager.objects.get(pk=pk)
    user = authmodel.User.objects.get(username=manager.utext)
    permission = Permission.objects.get(name=name)
    user.user_permissions.remove(permission)
    return redirect('user-perms',pk)

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def group_perms(request,name):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})
    group       = Group.objects.get(name=name)
    perms       = group.permissions.all()
    allperms    = Permission.objects.all()
    context     = {
        'perms'     : perms,
        'name'      : name,
        'allperms'  : allperms
    }
    return render(request,'auth/group-permission.html',context)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def add_group_perms(request,name):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})

    if request.method == "POST":
        pname = request.POST.get('pname')
        group = Group.objects.get(name=name)
        perm = Permission.objects.get(name=pname)
        group.permissions.add(perm)
        return redirect('group-perms',name)

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def del_group_perms(request,gname,name):
    perm = 0
    for i in request.user.groups.all():
        if i.name == 'Master_admin' : perm = 1
    
    if perm == 0:
        error = 'Access Denied'
        return render(request,'error.html',{'error':error})

    group = Group.objects.get(name=gname)
    perm = Permission.objects.get(name=name)
    group.permissions.remove(perm)
    return redirect('group-perms',name=gname)

#-------------------------------------------------------------------------------------------------------

def error_404(request,exception):
    return render(request,'authentication/404.html')
