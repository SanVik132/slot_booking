# Generated by Django 4.1.3 on 2022-11-17 14:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Saloon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('working_starttime', models.TimeField()),
                ('working_endtime', models.TimeField()),
                ('no_of_chairs', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cost', models.FloatField()),
                ('time_required', models.IntegerField()),
                ('saloon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.saloon')),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('saloon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.saloon')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
