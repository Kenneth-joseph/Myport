# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-20 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0013_auto_20200219_2045'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
