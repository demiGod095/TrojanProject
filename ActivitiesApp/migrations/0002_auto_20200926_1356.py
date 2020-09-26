# Generated by Django 3.0.8 on 2020-09-26 03:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('ActivitiesApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activitymodel',
            name='workCenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='auth.Group'),
        ),
        migrations.AlterField(
            model_name='historicalactivitymodel',
            name='workCenter',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='auth.Group'),
        ),
        migrations.DeleteModel(
            name='WorkCenterTypes',
        ),
    ]
