# Generated by Django 4.1.3 on 2022-11-17 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_booking_endtime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='time_required',
            field=models.IntegerField(),
        ),
    ]
