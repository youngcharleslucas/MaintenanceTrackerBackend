# Generated by Django 3.2.8 on 2021-12-16 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='Active', max_length=20),
            preserve_default=False,
        ),
    ]