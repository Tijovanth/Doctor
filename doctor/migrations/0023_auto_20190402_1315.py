# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-04-02 07:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0022_auto_20190402_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='Date',
            field=models.DateField(),
        ),
    ]