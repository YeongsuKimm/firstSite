# Generated by Django 5.0.1 on 2024-02-06 04:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbys', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role',
        ),
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(default=datetime.datetime(2024, 2, 6, 4, 21, 47, 356967, tzinfo=datetime.timezone.utc), max_length=50),
            preserve_default=False,
        ),
    ]
