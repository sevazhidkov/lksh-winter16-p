# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-03 06:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0004_auto_20170102_1814'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='answer_data',
            field=models.TextField(default='null'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='scoring_data',
            field=models.TextField(default='null'),
        ),
        migrations.AlterField(
            model_name='questionset',
            name='question_ids',
            field=models.TextField(default='null'),
        ),
    ]
