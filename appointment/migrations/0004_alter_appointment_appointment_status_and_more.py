# Generated by Django 4.2.7 on 2024-01-12 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_alter_appointment_appointment_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Running', 'Running')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_types',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=10),
        ),
    ]
