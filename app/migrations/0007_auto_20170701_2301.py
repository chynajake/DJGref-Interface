# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-01 17:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170701_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 1, 17, 1, 17, 385636, tzinfo=utc)),
        ),
    ]
