# Generated by Django 3.0.8 on 2020-11-07 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivitiesApp', '0006_auto_20201107_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitypartmodel',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='historicalactivitypartmodel',
            name='location',
            field=models.CharField(max_length=50, null=True),
        ),
    ]