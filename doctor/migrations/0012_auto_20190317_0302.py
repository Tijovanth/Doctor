# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-03-17 10:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0011_auto_20190314_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorprofileinfos',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]