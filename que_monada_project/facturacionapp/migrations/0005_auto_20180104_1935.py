# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-05 00:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacionapp', '0004_auto_20180104_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
    ]
