# Generated by Django 3.0.8 on 2020-10-10 05:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PartModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partNumber', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=20)),
                ('stockOnHand', models.IntegerField(blank=True)),
                ('minimumStock', models.IntegerField(blank=True)),
                ('reorderQtys', models.IntegerField(blank=True)),
                ('boxSize', models.IntegerField(blank=True)),
                ('leadtime', models.CharField(max_length=50)),
                ('weight', models.IntegerField(blank=True)),
                ('obsolete', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SupplierModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplierName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PartSupplierModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplierPartNumber', models.CharField(max_length=50, null=True)),
                ('preferred', models.BooleanField(default=False)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PartsApp.PartModel')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PartsApp.SupplierModel')),
            ],
        ),
        migrations.CreateModel(
            name='PartImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PartsApp.PartModel')),
            ],
        ),
        migrations.CreateModel(
            name='PartCommentModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('comment', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='PartsApp.PartModel')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalPartModel',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('partNumber', models.CharField(db_index=True, max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=20)),
                ('stockOnHand', models.IntegerField(blank=True)),
                ('minimumStock', models.IntegerField(blank=True)),
                ('reorderQtys', models.IntegerField(blank=True)),
                ('boxSize', models.IntegerField(blank=True)),
                ('leadtime', models.CharField(max_length=50)),
                ('weight', models.IntegerField(blank=True)),
                ('obsolete', models.BooleanField(default=False)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical part model',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
