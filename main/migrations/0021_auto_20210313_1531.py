# Generated by Django 3.1.5 on 2021-03-13 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20210313_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commands',
            name='nbPersonne',
        ),
        migrations.AlterField(
            model_name='commands',
            name='dateCommandePasse',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 15, 31, 58, 518951)),
        ),
        migrations.AlterField(
            model_name='galeriepic',
            name='dateUpload',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 15, 31, 58, 520925)),
        ),
        migrations.AlterField(
            model_name='shotgun',
            name='dateShotgun',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 15, 31, 58, 521982)),
        ),
        migrations.AlterField(
            model_name='shotgunconfig',
            name='dateCrea',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 3, 13, 15, 31, 58, 521982)),
        ),
    ]