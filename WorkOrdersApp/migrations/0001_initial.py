# Generated by Django 3.0.8 on 2020-09-15 10:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('PartsApp', '0001_initial'),
        ('ActivitiesApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskActivityModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startTime', models.DateTimeField(default=django.utils.timezone.now)),
                ('finishTime', models.DateTimeField(null=True)),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ActivitiesApp.ActivityModel')),
            ],
        ),
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.CharField(max_length=50)),
                ('fleetNumber', models.CharField(max_length=50)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='ActivitiesApp.GroupModel')),
            ],
        ),
        migrations.CreateModel(
            name='TaskPartsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('increment', models.BooleanField()),
                ('quantityRequired', models.IntegerField()),
                ('quantityCompleted', models.IntegerField(default=0)),
                ('activity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='WorkOrdersApp.TaskActivityModel')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PartsApp.PartModel')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='WorkOrdersApp.TaskModel')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='taskactivitymodel',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='WorkOrdersApp.TaskModel'),
        ),
        migrations.CreateModel(
            name='HistoricalTaskPartsModel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('increment', models.BooleanField()),
                ('quantityRequired', models.IntegerField()),
                ('quantityCompleted', models.IntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('activity', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='WorkOrdersApp.TaskActivityModel')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('part', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='PartsApp.PartModel')),
                ('task', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='WorkOrdersApp.TaskModel')),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical task parts model',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
