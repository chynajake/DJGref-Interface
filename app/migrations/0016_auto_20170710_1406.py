# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-07-10 08:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20170710_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 10, 8, 6, 55, 554037, tzinfo=utc)),
        ),
    ]
