# Generated by Django 4.1.2 on 2022-10-16 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0001_initial'),
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Name', models.CharField(max_length=50)),
                ('Profile_Url', models.URLField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Start_Date', models.DateField()),
                ('End_Date', models.DateField()),
                ('Reason', models.CharField(blank=True, help_text='add additional information for leave', max_length=255, null=True)),
                ('Approved_Status', models.CharField(blank=True, default='pending', max_length=12, null=True)),
                ('Approved_Description', models.CharField(blank=True, max_length=250, null=True)),
                ('is_approved', models.BooleanField(blank=True, default=False, null=True)),
                ('Leave_Type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='settings.leaves')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Emergency_Name', models.CharField(max_length=30)),
                ('Relationship', models.CharField(max_length=30)),
                ('Emergency_Phone', models.CharField(max_length=15)),
                ('Emergency_Email', models.EmailField(max_length=254)),
                ('Emergency_Address', models.CharField(max_length=250)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Document_Name', models.CharField(max_length=30)),
                ('Document_Type', models.CharField(max_length=30)),
                ('Document_File', models.FileField(default='default.pdf', upload_to='files/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Basic_Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('DOB', models.DateField(help_text='Please use the following format: <em>YYYY-MM-DD</em>.', null=True)),
                ('Address_1', models.CharField(help_text='Float no,Street address.', max_length=100, null=True)),
                ('Address_2', models.CharField(help_text='Apartment,Suite,Floor etc....', max_length=100, null=True)),
                ('City', models.CharField(max_length=30, null=True)),
                ('Postal_Code', models.CharField(max_length=10, null=True)),
                ('Religion', models.CharField(max_length=20, null=True)),
                ('Nationality', models.CharField(max_length=15, null=True)),
                ('Citizenship', models.CharField(max_length=20, null=True)),
                ('Blood_Group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='master.blood')),
                ('Country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='master.countries')),
                ('Martial_Status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='master.martial')),
                ('State', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='master.state')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Bank_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('Holder_Name', models.CharField(blank=True, max_length=20, null=True)),
                ('Account_No', models.CharField(blank=True, max_length=30, null=True)),
                ('Bank_Name', models.CharField(blank=True, max_length=30, null=True)),
                ('Branch_Location', models.CharField(blank=True, max_length=150, null=True)),
                ('IFSC', models.CharField(blank=True, max_length=30, null=True)),
                ('PAN', models.CharField(blank=True, max_length=10, null=True)),
                ('Aadhar', models.CharField(blank=True, max_length=12, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created_at',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddress', models.GenericIPAddressField()),
                ('latitude', models.CharField(blank=True, max_length=50, null=True)),
                ('longitude', models.CharField(blank=True, max_length=50, null=True)),
                ('Date', models.DateField(auto_now_add=True)),
                ('Manual_Dt', models.DateField(blank=True, null=True)),
                ('In_Time', models.TimeField(blank=True, null=True)),
                ('Out_Time', models.TimeField(blank=True, null=True)),
                ('Late_Time', models.TimeField(blank=True, null=True)),
                ('Early_Leaving', models.TimeField(blank=True, null=True)),
                ('Total_Working_Hours', models.TimeField(blank=True, null=True)),
                ('Over_Time', models.TimeField(blank=True, null=True)),
                ('Clock_In', models.BooleanField(blank=True, default=False, null=True)),
                ('Clock_Out', models.BooleanField(blank=True, default=False, null=True)),
                ('Present', models.BooleanField(blank=True, default=False, null=True)),
                ('Absent', models.BooleanField(blank=True, default=False, null=True)),
                ('Half_Day', models.BooleanField(blank=True, default=False, null=True)),
                ('Late', models.BooleanField(blank=True, default=False, null=True)),
                ('Leave', models.BooleanField(blank=True, default=False, null=True)),
                ('Reason', models.CharField(blank=True, max_length=250, null=True)),
                ('Status', models.CharField(blank=True, default='Absent', max_length=30, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
