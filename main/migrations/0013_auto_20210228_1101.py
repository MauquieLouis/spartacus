# Generated by Django 3.1.5 on 2021-02-28 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210226_1852'),
    ]

    operations = [
        migrations.AddField(
            model_name='commands',
            name='type',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
        migrations.AlterField(
            model_name='commands',
            name='dateCommandePasse',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 28, 11, 1, 58, 682770)),
        ),
    ]