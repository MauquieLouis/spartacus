# Generated by Django 3.1.5 on 2021-03-13 12:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20210313_0025'),
    ]

    operations = [
        migrations.AddField(
            model_name='commands',
            name='nbPersonne',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='commands',
            name='dateCommandePasse',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 13, 49, 2, 363365)),
        ),
        migrations.AlterField(
            model_name='galeriepic',
            name='dateUpload',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 13, 49, 2, 365359)),
        ),
        migrations.AlterField(
            model_name='shotgun',
            name='dateShotgun',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 13, 49, 2, 366356)),
        ),
        migrations.AlterField(
            model_name='shotgunconfig',
            name='dateCrea',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 13, 49, 2, 366356)),
        ),
    ]