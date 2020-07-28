# Generated by Django 3.0.8 on 2020-07-25 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('PartsApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ActivitiesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkCentreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle', models.CharField(max_length=50)),
                ('increment', models.BooleanField(default=False)),
                ('quantityRequired', models.IntegerField()),
                ('quantityCompleted', models.IntegerField(default=0)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ActivitiesApp.ActivityModel')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PartsApp.PartModel')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ActivitiesApp.TaskModel')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]