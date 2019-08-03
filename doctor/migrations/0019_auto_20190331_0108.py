# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-03-31 08:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0018_auto_20190323_0402'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appoinment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Slot_No', models.IntegerField(blank=True)),
                ('Date', models.DateTimeField(default=django.utils.timezone.now)),
                ('Reason_to_visit', models.TextField(max_length=1000)),
                ('Doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.DoctorProfileInfos')),
            ],
        ),
        migrations.RemoveField(
            model_name='appoinmentbooking',
            name='BookedDoctor',
        ),
        migrations.RemoveField(
            model_name='appoinmentbooking',
            name='Bookingperson',
        ),
        migrations.AlterField(
            model_name='location',
            name='Availability',
            field=models.CharField(choices=[('1', 'All days'), ('0', 'Mon-Fri')], max_length=200),
        ),
        migrations.DeleteModel(
            name='AppoinmentBooking',
        ),
        migrations.AddField(
            model_name='appoinment',
            name='Loc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Location'),
        ),
        migrations.AddField(
            model_name='appoinment',
            name='User',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.UserProfileInfo'),
        ),
    ]
