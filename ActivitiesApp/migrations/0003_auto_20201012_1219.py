# Generated by Django 3.0.8 on 2020-10-12 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivitiesApp', '0002_groupactivitymodel_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitypartmodel',
            name='order',
            field=models.IntegerField(default=100000),
        ),
        migrations.AddField(
            model_name='historicalactivitypartmodel',
            name='order',
            field=models.IntegerField(default=100000),
        ),
    ]
