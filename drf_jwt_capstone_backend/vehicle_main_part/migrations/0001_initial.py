# Generated by Django 3.2.8 on 2021-12-20 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('maintenance_item', '0001_initial'),
        ('vehicle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VehicleMainPart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('main_part_name', models.CharField(max_length=50)),
                ('main_part_description', models.CharField(max_length=100)),
                ('maintenance_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance_item.maintenanceitem')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle')),
            ],
        ),
    ]