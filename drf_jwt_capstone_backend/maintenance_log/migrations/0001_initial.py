# Generated by Django 3.2.8 on 2022-01-03 23:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maintenance_item', '0003_auto_20211231_1750'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vehicle', '0003_vehicle_miles_current'),
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_miles', models.IntegerField()),
                ('log_note', models.CharField(max_length=300)),
                ('log_date', models.DateField()),
                ('complete', models.BooleanField(default=False)),
                ('maintenance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance_item.maintenanceitem')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle')),
            ],
        ),
    ]
