# Generated by Django 3.0 on 2021-08-02 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0006_auto_20210802_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='start_timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
