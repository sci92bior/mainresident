# Generated by Django 4.2.6 on 2023-12-03 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('device_manager', '0003_remove_authenticateddevice_device_port'),
    ]

    operations = [
        migrations.AddField(
            model_name='authenticateddevice',
            name='hdl_ip',
            field=models.CharField(default='1234', max_length=50, unique=True),
            preserve_default=False,
        ),
    ]
