# Generated by Django 3.0.8 on 2020-11-07 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivitiesApp', '0005_auto_20201022_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitypartmodel',
            name='location',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalactivitypartmodel',
            name='location',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
