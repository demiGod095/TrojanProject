# Generated by Django 3.0.8 on 2020-10-21 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivitiesApp', '0003_auto_20201012_1219'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitypartmodel',
            name='location',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AddField(
            model_name='historicalactivitypartmodel',
            name='location',
            field=models.CharField(max_length=4, null=True),
        ),
    ]
