# Generated by Django 3.0.8 on 2020-10-13 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ActivitiesApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupactivitymodel',
            name='order',
            field=models.IntegerField(default=100000),
        ),
    ]