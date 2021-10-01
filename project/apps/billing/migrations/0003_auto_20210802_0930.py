# Generated by Django 3.0 on 2021-08-02 09:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0002_auto_20210802_0912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='users',
        ),
        migrations.AlterField(
            model_name='subscription',
            name='start_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 2, 9, 30, 20, 344019, tzinfo=utc)),
        ),
    ]
