# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-01-01 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answerset',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
    ]
