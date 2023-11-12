# Generated by Django 4.2.6 on 2023-11-12 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('decision_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='challengeresponseentity',
            name='conditions',
        ),
        migrations.AddField(
            model_name='challengeresponseentity',
            name='conditions',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='decision_module.crcondition'),
        ),
    ]
