# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-10 00:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('purchases', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='date',
            field=models.DateField(default=datetime.datetime(2016, 4, 10, 0, 16, 8, 382255, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
