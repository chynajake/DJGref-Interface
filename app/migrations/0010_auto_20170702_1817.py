# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-02 12:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20170701_2326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 2, 12, 17, 51, 876231, tzinfo=utc)),
        ),
    ]
