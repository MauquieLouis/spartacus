# Generated by Django 3.1.5 on 2021-04-19 11:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20210419_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commands',
            name='dateCommandePasse',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 13, 51, 21, 580251)),
        ),
        migrations.AlterField(
            model_name='eventqrcode',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 13, 51, 21, 582246)),
        ),
        migrations.AlterField(
            model_name='galeriepic',
            name='dateUpload',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 13, 51, 21, 581249)),
        ),
        migrations.AlterField(
            model_name='match',
            name='dateMatch',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='pronostic',
            name='dateProno',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 13, 51, 21, 583243)),
        ),
        migrations.AlterField(
            model_name='shotgun',
            name='dateShotgun',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 13, 51, 21, 581249)),
        ),
        migrations.AlterField(
            model_name='shotgunconfig',
            name='dateCrea',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 13, 51, 21, 582246)),
        ),
    ]
