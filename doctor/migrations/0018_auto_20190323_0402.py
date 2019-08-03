# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-03-23 11:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0017_auto_20190321_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LocationName', models.CharField(max_length=200)),
                ('LocationAddress', models.TextField(max_length=500)),
                ('TimingFrom', models.TimeField()),
                ('TimingTo', models.TimeField()),
                ('slot', models.PositiveIntegerField()),
                ('Availability', models.CharField(choices=[('All days', '1'), ('Mon-Fri', '0')], max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='doctorprofileinfos',
            name='workinglocation',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='location',
            name='Doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.DoctorProfileInfos'),
        ),
    ]
