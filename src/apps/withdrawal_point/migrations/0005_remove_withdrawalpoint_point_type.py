# Generated by Django 2.1.3 on 2018-11-09 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('withdrawal_point', '0004_auto_20181109_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='withdrawalpoint',
            name='point_type',
        ),
    ]