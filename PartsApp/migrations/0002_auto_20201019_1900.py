# Generated by Django 3.0.8 on 2020-10-19 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PartsApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalpartmodel',
            name='location',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='partmodel',
            name='location',
            field=models.CharField(max_length=40),
        ),
    ]