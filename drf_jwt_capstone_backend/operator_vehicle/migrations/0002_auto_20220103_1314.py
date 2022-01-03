# Generated by Django 3.2.8 on 2022-01-03 20:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0003_vehicle_miles_current'),
        ('operator_vehicle', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatorvehicle',
            name='operator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='operatorvehicle',
            name='vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle'),
        ),
    ]
