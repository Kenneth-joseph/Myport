# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-19 08:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0010_auto_20200219_1112'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='name',
        ),
    ]
