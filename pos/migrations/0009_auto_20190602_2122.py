# Generated by Django 2.2.1 on 2019-06-02 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pos', '0008_orderitem_qty'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qty',
            new_name='jml',
        ),
    ]
