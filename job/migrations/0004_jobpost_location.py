# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-03 09:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0003_jobapplication'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobpost',
            name='location',
            field=models.CharField(default='Dhaka', max_length=150),
            preserve_default=False,
        ),
    ]