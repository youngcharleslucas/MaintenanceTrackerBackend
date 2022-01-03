# Generated by Django 3.2.8 on 2022-01-03 20:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0003_vehicle_miles_current'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('operator_vehicle', '0002_auto_20220103_1314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operatorvehicle',
            name='operator',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='authentication.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='operatorvehicle',
            name='vehicle',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle'),
            preserve_default=False,
        ),
    ]