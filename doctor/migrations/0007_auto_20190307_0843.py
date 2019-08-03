# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-03-07 16:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('doctor', '0006_auto_20190307_0818'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorProfileInfos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('workinglocation', models.TextField()),
                ('profile_pic', models.ImageField(blank=True, upload_to='profile_pics')),
                ('certificate', models.ImageField(blank=True, upload_to='certificate_pics')),
                ('specialist', models.TextField()),
                ('doctor', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctorprofileinfo',
            name='doctor',
        ),
        migrations.DeleteModel(
            name='DoctorProfileInfo',
        ),
    ]
