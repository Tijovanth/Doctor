# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-04-01 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0020_auto_20190331_0950'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoinment',
            name='Date',
            field=models.DateField(),
        ),
    ]