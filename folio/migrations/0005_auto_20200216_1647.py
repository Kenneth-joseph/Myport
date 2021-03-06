# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-02-16 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0004_project_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='content',
            field=models.CharField(default='kent', max_length=30),
        ),
        migrations.AddField(
            model_name='rating',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='folio.Project'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='rating',
            name='usability',
            field=models.CharField(default='kent', max_length=30),
        ),
        migrations.AlterField(
            model_name='rating',
            name='design',
            field=models.CharField(default='kent', max_length=30),
        ),
    ]
