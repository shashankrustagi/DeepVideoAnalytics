# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-23 07:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dvaapp', '0039_worker_alive'),
    ]

    operations = [
        migrations.AddField(
            model_name='tevent',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dvaapp.Worker'),
        ),
    ]
