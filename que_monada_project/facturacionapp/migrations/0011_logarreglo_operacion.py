# Generated by Django 2.0 on 2018-02-02 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacionapp', '0010_auto_20180202_0312'),
    ]

    operations = [
        migrations.AddField(
            model_name='logarreglo',
            name='operacion',
            field=models.CharField(default='Borrado', max_length=20),
        ),
    ]
