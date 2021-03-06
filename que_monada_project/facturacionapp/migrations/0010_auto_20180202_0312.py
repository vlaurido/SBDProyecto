# Generated by Django 2.0 on 2018-02-02 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facturacionapp', '0009_auto_20180118_0941'),
    ]

    operations = [
        migrations.CreateModel(
            name='LogArreglo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('cod_arreglo', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'LogArreglos',
                'verbose_name': 'LogArreglo',
            },
        ),
        migrations.AlterField(
            model_name='factura',
            name='tipo_pago',
            field=models.CharField(choices=[('CREDITO', 'Crédito'), ('EFECTIVO', 'Efectivo')], default='EFECTIVO', max_length=20),
        ),
    ]
