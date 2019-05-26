# Generated by Django 2.2.1 on 2019-05-26 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0003_auto_20190526_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='meja',
        ),
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.RemoveField(
            model_name='order',
            name='success',
        ),
        migrations.RemoveField(
            model_name='order',
            name='timestamp',
        ),
        migrations.AlterField(
            model_name='karyawan',
            name='tugas',
            field=models.CharField(choices=[('1', 'kasir'), ('2', 'pelayan')], max_length=8),
        ),
        migrations.AlterField(
            model_name='product',
            name='stok',
            field=models.CharField(choices=[('1', 'ready'), ('0', 'notready')], max_length=9),
        ),
    ]
