# Generated by Django 2.1.3 on 2018-11-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('withdrawal_point', '0002_auto_20181108_1849'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='is_closed',
            field=models.BooleanField(default=False, verbose_name='is closed?'),
        ),
    ]