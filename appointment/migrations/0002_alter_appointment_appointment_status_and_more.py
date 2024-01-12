# Generated by Django 4.2.7 on 2024-01-07 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_status',
            field=models.CharField(choices=[('Completed', 'Completed'), ('Running', 'Running'), ('Pending', 'Pending')], default='Pending', max_length=10),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='appointment_types',
            field=models.CharField(choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=10),
        ),
    ]
