# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 18:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacionapp', '0003_auto_20180104_1049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='arreglo',
            options={'verbose_name': 'Arreglo', 'verbose_name_plural': 'Arreglos'},
        ),
        migrations.AlterModelOptions(
            name='toalla',
            options={'verbose_name': 'Toalla', 'verbose_name_plural': 'Toallas'},
        ),
        migrations.AddField(
            model_name='arreglo',
            name='borrado',
            field=models.BooleanField(default=False),
        ),
    ]
