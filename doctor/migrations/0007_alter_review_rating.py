# Generated by Django 4.2.7 on 2024-01-12 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0006_alter_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('✸✸✸', '✸✸✸'), ('✸', '✸'), ('✸✸✸✸✸', '✸✸✸✸✸'), ('✸✸', '✸✸'), ('✸✸✸✸', '✸✸✸✸')], max_length=100),
        ),
    ]
