# Generated by Django 4.2.7 on 2024-01-07 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0003_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('✸✸✸', '✸✸✸'), ('✸✸✸✸✸', '✸✸✸✸✸'), ('✸', '✸'), ('✸✸✸✸', '✸✸✸✸'), ('✸✸', '✸✸')], max_length=100),
        ),
    ]