# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 15:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacionapp', '0002_auto_20180104_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arreglo',
            name='canasta',
            field=models.CharField(choices=[('SI', 'Si'), ('NO', 'No')], max_length=50),
        ),
        migrations.AlterField(
            model_name='arreglo',
            name='grabado',
            field=models.CharField(choices=[('SI', 'Si'), ('NO', 'No')], max_length=50),
        ),
        migrations.AlterField(
            model_name='arreglo',
            name='tamanio',
            field=models.CharField(choices=[('PEQUEÑO', 'Pequeño'), ('MEDIANO', 'Mediano'), ('GRANDE', 'Grande')], max_length=50),
        ),
    ]