# Generated by Django 3.1.5 on 2021-05-02 17:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_auto_20210502_1813'),
    ]

    operations = [
        migrations.AddField(
            model_name='campagnecommande',
            name='valid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='campagnecommande',
            name='dateCommandePasse',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 2, 19, 2, 25, 246192)),
        ),
        migrations.AlterField(
            model_name='commands',
            name='dateCommandePasse',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 2, 19, 2, 25, 236410)),
        ),
        migrations.AlterField(
            model_name='eventqrcode',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 2, 19, 2, 25, 242358)),
        ),
        migrations.AlterField(
            model_name='galeriepic',
            name='dateUpload',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 2, 19, 2, 25, 239192)),
        ),
        migrations.AlterField(
            model_name='pronostic',
            name='dateProno',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 2, 19, 2, 25, 245157)),
        ),
        migrations.AlterField(
            model_name='shotgun',
            name='dateShotgun',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 2, 19, 2, 25, 240192)),
        ),
        migrations.AlterField(
            model_name='shotgunconfig',
            name='dateCrea',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 2, 19, 2, 25, 241198)),
        ),
    ]
