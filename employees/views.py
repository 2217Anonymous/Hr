from django.http import HttpResponseRedirect
from django.shortcuts import render,redirect
from master import models as master
from django.contrib import messages
from employees import forms
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from ipware import get_client_ip
from datetime import datetime,time,timedelta
from django.utils import timezone
from helpers.models import datetime_convert,time_convert,time_calculator
import calendar
from django import template

from authentication import models as auth
from employees import models as employeeModel
from settings import models as settingsmodel
from master import models as mastermodel

register = template.Library()
# Create your views here.
#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def employee_dashboard(request):
    data        = settingsmodel.Theme_Settings.objects.all()
    leave_type  = settingsmodel.Leaves.objects.filter(status=True)
    current_date    = datetime.today().date()
    btn_visible     = employeeModel.Attendance.objects.filter(user=request.user,Date=current_date).values('Clock_In','Clock_Out')
    check_entry     = employeeModel.Attendance.objects.filter(user=request.user,Date=current_date,Clock_In=True).exists()
    context = {
        'dt'         : data,
        'leave_type' : leave_type,
        'check'      : check_entry,
        'btn'        : btn_visible,
    }
    user            = request.user.id
    print("uaer id is :",user)
    return render(request,'employee/employee-dashboard.html',context)

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def employee_details(request):
    blood           = master.Blood.objects.filter(status=True)
    country         = master.Countries.objects.all()
    state           = master.State.objects.all() 
    martial         = master.Martial.objects.filter(status=True)
    emp_detalis     = employeeModel.Basic_Employee.objects.filter(user=request.user)
    bank_details    = employeeModel.Bank_Details.objects.filter(user=request.user)
    emp_doc         = employeeModel.Documents.objects.filter(user=request.user)
    emp_contact     = employeeModel.Emergency.objects.filter(user=request.user)
    social          = employeeModel.Social.objects.filter(user=request.user) 
    context = {
        'Blood_Data'            : blood,
        'Country_Data'          : country,
        'State_Data'            : state,
        'Martial_Data'          : martial,
        'Employee_Details'      : emp_detalis,
        'Bank_Details'          : bank_details,
        'Employee_Documents'    : emp_doc,
        'Emergency_Contact'     : emp_contact,
        'Social'                : social,
    }
    return render(request,'employee/employee-details.html',context) 

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def employee_list(request):
    employee = auth.User.objects.all()
    context = {
        'tbl_data' : employee
    }
    return render(request,'employee/employee.html',context)

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def delete_employee_details(request,pk):
    try:
        employee_details = employeeModel.Basic_Employee.objects.get(id=pk,user=request.user)
        employee_details.delete()
        messages.success(request,'User deleted Successfully...!')
        return HttpResponseRedirect(reverse('employee-details'))
    except employeeModel.Bank_Details.DoesNotExist:
        messages.error(request,'You are not allowed...!')
        return HttpResponseRedirect(reverse('employee-list'))

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def bank_details(request):
    if request.method == 'POST':
        form = forms.Bank_Details_Form(request.POST)
        if form.is_valid():
            user            = request.user.id
            holder_name     = request.POST.get('Holder_Name')
            account_no      = request.POST.get('Account_No')
            bank_name       = request.POST.get('Bank_Name')
            branch_location = request.POST.get('Branch_Location')
            ifsc            = request.POST.get('IFSC')
            pan             = request.POST.get('PAN')
            aadhar          = request.POST.get('Aadhar')
            form = employeeModel.Bank_Details.objects.create(
                user_id         = user,
                Holder_Name     = holder_name,
                Account_No      = account_no,
                Bank_Name       = bank_name,
                Branch_Location = branch_location,
                IFSC            = ifsc,
                PAN             = pan,
                Aadhar          = aadhar,
                    )
            form.save()
            messages.success(request,'Bank Details Successfull added!')
            return HttpResponseRedirect(reverse('employee-details'))
        else:
            messages.error(request,'Form is not valid..!')
            return HttpResponseRedirect(reverse('employee-details'))
    return redirect('employee-details')

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def delete_bank_details(request,pk):
    try:
        bank_detail = employeeModel.Bank_Details.objects.get(id=pk,user=request.user)
        bank_detail.delete()
        messages.success(request,'User deleted Successfully...!')
        return HttpResponseRedirect(reverse('employee-details'))
    except employeeModel.Bank_Details.DoesNotExist:
        messages.error(request,'You are not allowed...!')
        return HttpResponseRedirect(reverse('employee-details'))

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def edit_bank_details(request):
    if request.method == 'POST':
        id   = request.POST.get('id')
        form = forms.Bank_Details_Form(request.POST)
        if form.is_valid():
            user            = request.user.id
            holder_name     = request.POST.get('Holder_Name')
            account_no      = request.POST.get('Account_No')
            bank_name       = request.POST.get('Bank_Name')
            branch_location = request.POST.get('Branch_Location')
            ifsc            = request.POST.get('IFSC')
            pan             = request.POST.get('PAN')
            aadhar          = request.POST.get('Aadhar')
            employeeModel.Bank_Details.objects.filter(pk=id,user_id=request.user.id).update(
                user_id         = user,
                Holder_Name     = holder_name,
                Account_No      = account_no,
                Bank_Name       = bank_name,
                Branch_Location = branch_location,
                IFSC            = ifsc,
                PAN             = pan,
                Aadhar          = aadhar,
                )
            messages.success(request,'updated successfully...!')
            return HttpResponseRedirect(reverse('employee-details'))
        else:
            messages.error(request,'Form is not updated...!')
            return HttpResponseRedirect(reverse('employee-details'))
    return redirect('employee-details')

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def emp_documents(request):
    if request.method == 'POST':
        form = forms.Employee_Documents_Form(request.POST,request.FILES)
        if form.is_valid():
            user         = request.user.id
            doc_name     = request.POST.get('Document_Name')
            doc_type     = request.POST.get('Document_Type')
            doc_file     = request.FILES['Document_File']

            form = employeeModel.Documents.objects.create(
                user_id         = user,
                Document_Name   = doc_name,
                Document_Type   = doc_type,
                Document_File   = doc_file,
                    )
            form.save()
            messages.success(request,'Documents Successfull Upload!')
            return HttpResponseRedirect(reverse('employee-details'))
        else:
            messages.error(request,'Form is not valid..!')
            return HttpResponseRedirect(reverse('employee-details'))
    return render(request,'employee/employee-details.html')

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def delete_emp_documents(request,pk):
    try:
        emp_doc = employeeModel.Documents.objects.get(id=pk,user=request.user)
        emp_doc.delete()
        messages.success(request,'File deleted Successfully...!')
        return HttpResponseRedirect(reverse('employee-details'))
    except employeeModel.Bank_Details.DoesNotExist:
        messages.error(request,'You are not allowed...!')
        return HttpResponseRedirect(reverse('employee-details'))

#-------------------------------------------------------------------------------------------------------

login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def emg_contact(request):
    if request.method == 'POST':
        form = forms.Emergency_Contact_Form(request.POST)
        if form.is_valid():
            user            = request.user.id
            emg_name        = request.POST.get('Emergency_Name')
            relationship    = request.POST.get('Relationship')
            emg_address     = request.POST.get('Emergency_Address')
            emg_email       = request.POST.get('Emergency_Email')
            emg_phone       = request.POST.get('Emergency_Phone')
            form            = employeeModel.Emergency.objects.create(
                user_id             = user,
                Emergency_Name      = emg_name,
                Relationship        = relationship,
                Emergency_Address   = emg_address,
                Emergency_Email     = emg_email,
                Emergency_Phone     = emg_phone,
                    )
            form.save()
            messages.success(request,'Form  successfull added!')
            return HttpResponseRedirect(reverse('employee-details'))
        else:
            messages.error(request,'Form is not valid..!')
            return HttpResponseRedirect(reverse('employee-details'))
    return redirect('employee-details')

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def delete_emg_contact(request,pk):
    try:
        emg_contact = employeeModel.Emergency.objects.get(id=pk,user=request.user)
        emg_contact.delete()
        messages.success(request,'File deleted Successfully...!')
        return HttpResponseRedirect(reverse('employee-details'))
    except employeeModel.Bank_Details.DoesNotExist:
        messages.error(request,'You are not allowed...!')
        return HttpResponseRedirect(reverse('employee-details'))

#-------------------------------------------------------------------------------------------------------

login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def social_media(request):
    if request.method == 'POST':
        form = forms.Social_Media_Form(request.POST)
        if form.is_valid():
            user            = request.user.id
            socila_name     = request.POST.get('Name')
            profile         = request.POST.get('Profile_Url')
            form            = employeeModel.Social.objects.create(
                user_id     = user,
                Name        = socila_name,
                Profile_Url = profile,
                    )
            form.save()
            messages.success(request,'Form successfull added!')
            return HttpResponseRedirect(reverse('employee-details'))
        else:
            messages.error(request,'Form is not valid..!')
            return HttpResponseRedirect(reverse('employee-details'))
    return redirect('employee-details')

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def delete_social_media(request,pk):
    try:
        social_media = employeeModel.Social.objects.get(id=pk,user=request.user)
        social_media.delete()
        messages.success(request,'Data deleted Successfully...!')
        return HttpResponseRedirect(reverse('employee-details'))
    except employeeModel.Bank_Details.DoesNotExist:
        messages.error(request,'You are not allowed...!')
        return HttpResponseRedirect(reverse('employee-details'))

#-------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def leave(request):
    leaves = employeeModel.Leave.objects.filter(user=request.user)
    leave_type = settingsmodel.Leaves.objects.filter(status=True)
    context = {
        'leave_data' : leaves,
        'leave_type' : leave_type,
    }
    return render(request,'request/leave.html',context)

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def leave_request(request):
    if request.method == 'POST':
        form = forms.Leave_Request_Form(request.POST)
        
        if form.is_valid():
            user           = request.user.id
            start_dt       = request.POST.get('Start_Date')
            end_dt         = request.POST.get('End_Date')
            leave_type     = request.POST.get('Leave_Type')
            reason         = request.POST.get('Reason')
            form           = employeeModel.Leave.objects.create(
                user_id         = user,
                Start_Date      = start_dt,
                End_Date        = end_dt,
                Leave_Type_id   = leave_type,
                Reason          = reason,
                    )
            form.save()
            messages.success(request,'Leave Request Send!')
            return redirect('leave')
        else:
            messages.error(request,'Form is not valid..!')
            return redirect('leave')
    return redirect('leave')

#-------------------------------------------------------------------------------------------------------

def leave_application(request):
    leave_request = employeeModel.Leave.objects.all
    context = {
        'leave_data' : leave_request,
    }
    return render(request,'hr-approval/leave-application.html',context)

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def leave_approval(request):
    if request.method == 'POST':
        id          = request.POST.get('id')
        description = request.POST.get('Approved_Description')
        isapproved  = request.POST.get('is_approved')
        if isapproved == "True" :
            approved = employeeModel.Leave.objects.filter(id=id,is_approved=True)
            if not approved:
                employeeModel.Leave.objects.filter(id=id).update(Approved_Description=description,Approved_Status="Approved",is_approved=isapproved)
                messages.success(request,'Leave has been approved')
                return redirect('leave-application')
            else:
                messages.warning(request,'Leave have been already approved...!')
                return redirect('leave-application')

        elif isapproved == "False" :
            employeeModel.Leave.objects.filter(id=id).update(Approved_Description=description,Approved_Status="Rejected",is_approved=isapproved)
            messages.success(request,'Leave has been rejected')
            return redirect('leave-application')
        else:                
            messages.warning(request,'Leave have been already rejected...!')
            return redirect('leave-application')
    return redirect('leave-application')
#-------------------------------------------------------------------------------------------------------
    
    #ATTENdance

#-------------------------------------------------------------------------------------------------------

@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def attendance(request):
    current_date    = datetime.today().date()
    btn_visible     = employeeModel.Attendance.objects.filter(user=request.user,Date=current_date).values('Clock_In','Clock_Out')
    check_entry     = employeeModel.Attendance.objects.filter(user=request.user,Date=current_date,Clock_In=True).exists()
    attendance      = employeeModel.Attendance.objects.filter(user=request.user) 
    dt_Dept         = mastermodel.Departments.objects.filter(status=True)
    dt_Employee     = auth.User.objects.all()
    context = {
        'check'         : check_entry,
        'btn'           : btn_visible,
        'my_attendance' : attendance,
        'drop_data'     : dt_Dept,
        'drop_emp'      : dt_Employee
    }
    return render(request,"employee/attendance.html",context)

#-------------------------------------------------------------------------------------------------------
@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def In(request):
    current_date    = datetime.today().date()
    check_entry     = employeeModel.Attendance.objects.filter(user=request.user,Date=current_date).exists()
    if check_entry:
        messages.error(request,'You are already in')
    else:
        if request.method == "POST":
            form            = forms.Attendance_Form(request.POST)
            Present_Time    = datetime_convert(datetime.today())
            office_in_time  = datetime_convert(time(10,0,0,0))
            late_time       = time_calculator.sub_time(Present_Time,office_in_time)
            user            = request.user.id
            In_Time         = Present_Time
            ipaddress       = get_client_ip(request)
            
            latitude        = request.POST.get('latitude')
            longitude       = request.POST.get('longitude')
            print("--------------------------------------")
            print("Latitude is ",latitude)
            print("Longitude is ",longitude)
            print("--------------------------------------")
            if form.is_valid():                
                #--------------
                # Insert Data's
                #--------------
                form        = employeeModel.Attendance.objects.create(
                user_id     = user,
                In_Time     = In_Time,
                Late_Time   = "0:0:0" if late_time <= "0:0:0" else late_time,
                Clock_In    = True,
                Clock_Out   = False,
                Present     = True,
                Absent      = False,
                Half_Day    = False,
                Late        = False if late_time <= "0:0:0" else True,
                Leave       = False,
                Status      = 'Present',    
                ipaddress   = ipaddress,
                latitude    = latitude,
                longitude   = longitude,
                )
                form.save()
                messages.success(request,'You are in')
            else:
                messages.error(request,'Form are not valid')
    return redirect('attendance')

#-------------------------------------------------------------------------------------------------------
@login_required(login_url='login')
@user_passes_test(lambda user: user.is_employee)
def Out(request):
    current_date = datetime.today().date()
    check_entry  = employeeModel.Attendance.objects.filter(user=request.user,Date=current_date,Clock_In=True).exists()
    present_time = employeeModel.Attendance.objects.get(user=request.user,Date=current_date).In_Time

    if request.method == "POST":
        dt                  = datetime.today()
        OutTime             = datetime_convert(datetime.today())
        office_out_time     = datetime_convert(time(18,0,0,0))
        office_working_hrs  = datetime_convert(time(8,0,0,0))
        In                  = datetime_convert(present_time)
        
        over_time = timedelta(
            hours   = office_working_hrs.hour,
            minutes = office_working_hrs.minute,
        )

        early       = office_out_time - OutTime
        
        total_hour  = OutTime - In
        overtime    = total_hour - over_time
        
        early_time      = str(early) 
        working_hour    = str(total_hour)
        over_time       = str(overtime)
        
        if check_entry:    
            employeeModel.Attendance.objects.filter(user = request.user,Date = dt).update(
                Out_Time            = OutTime,
                Early_Leaving       = "0:0:0" if early_time <= "0:0:0" else early_time,
                Total_Working_Hours = working_hour,
                Over_Time           = "0:0:0" if over_time <= "0:0:0" else over_time,
                Clock_In            = False,
                Clock_Out           = True,
                Half_Day            = True if str(working_hour) == "4:0:0" else False,
                Leave               = True if str(working_hour) < "4:0:0" else False,
            )
            messages.success(request,'You\'r logout')
        else:
            messages.warning(request,'You\'r not present')
    return redirect('attendance')

#-------------------------------------------------------------------------------------------------------
@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def attendance_list(request):
    start_date              = datetime.today().date()
    get_month               = datetime.now().month
    days_in_current_month   = calendar.monthrange(start_date.year,start_date.month)[1]
    attendance              = employeeModel.Attendance.objects.all()
    day_list                = days_in_current_month
    att                     = employeeModel.Attendance.objects.filter(Date__gte=datetime.today().date())
    context = {
        'daycount'      : range(1,day_list+1),
        'total_days'    : days_in_current_month,
        'att_list'      : attendance,
        'month'         : get_month,
        'date'          : att,
    }
    return render(request,'employee/attendance-list.html',context)


#-------------------------------------------------------------------------------------------------------
@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def employee_attendance(request):
    attendance      = employeeModel.Attendance.objects.all
    context = {
        "emp_att" : attendance
    }
    return render(request,"employee/employee-attendance.html",context)
#-------------------------------------------------------------------------------------------------------
@login_required(login_url='login')
@user_passes_test(lambda user: user.is_admin)
def manual_attendance(request):
    emp_data    = auth.User.objects.all()
    userId      = request.POST.get('user')
    manual_dt   = request.POST.get('Manual_Dt')
    check_entry = employeeModel.Attendance.objects.filter(user=userId,Date=manual_dt).exists()
    manual_att  = employeeModel.Attendance.objects.all() 

    context = {
        'drop_data' : emp_data,
        'attendance': manual_att,
    }

    if request.method == "POST":
        userId              = userId
        manual_dt           = manual_dt 

        _in                 = request.POST.get('In_Time')
        in_time             = time_convert(_in) 

        _out                = request.POST.get('Out_Time')
        out_time            = time_convert(_out)

        reason              = request.POST.get('Reason')

        ipaddress           = get_client_ip(request)
        latitude            = request.POST.get('latitude')
        longitude           = request.POST.get('longitude')

        office_in_time      = datetime_convert(time(10,0,0,0))
        office_out_time     = datetime_convert(time(18,0,0,0))
        office_working_hrs  = datetime_convert(time(8,0,0,0))

        over_time = timedelta(
            hours   = office_working_hrs.hour,
            minutes = office_working_hrs.minute,
        )

        early_      = office_out_time   - out_time
        total_hour  = out_time          - in_time
        overtime_   = total_hour        - over_time  
        late_       = time_calculator.sub_time(in_time,office_in_time)

        late_time   = str(late_)
        overtime    = str(overtime_)
        early       = str(early_)
        
        if check_entry:
            messages.warning(request,'already Submited')
            return redirect('manual-attendance')
        else:
            form        = employeeModel.Attendance.objects.create(
            user_id             = userId,
            Manual_Dt           = manual_dt,
            In_Time             = in_time,
            Out_Time            = out_time,
            Late_Time           = "0:0:0" if late_time <= "0:0:0" else late_time,
            Early_Leaving       = "0:0:0" if early <= "0:0:0" else early,
            Total_Working_Hours = str(total_hour),
            Over_Time           = "0:0:0" if overtime <= "0:0:0" else overtime,
            Clock_In            = False,
            Clock_Out           = True,
            Present             = True,
            Absent              = False,
            Half_Day            = True if str(total_hour) == "4:0:0" else False,
            Late                = False if late_time <= "0:0:0" else True,
            Leave               = True if str(total_hour) < "4:0:0" else False,
            Status              = 'Present',
            Reason              = reason, 
            ipaddress           = ipaddress,
            latitude            = latitude,
            longitude           = longitude,
            )
            form.save()
            messages.success(request,'Attendance Submited')
            return redirect('manual-attendance')  
    return render(request,"employee/manual-attendance.html",context)

#-------------------------------------------------------------------------------------------------------
