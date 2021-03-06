# Generated by Django 3.1.5 on 2021-04-21 12:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_auto_20210421_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commands',
            name='dateCommandePasse',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 21, 14, 55, 46, 733586)),
        ),
        migrations.AlterField(
            model_name='eventqrcode',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 21, 14, 55, 46, 736606)),
        ),
        migrations.AlterField(
            model_name='galeriepic',
            name='dateUpload',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 21, 14, 55, 46, 734612)),
        ),
        migrations.AlterField(
            model_name='match',
            name='isFinish',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='pronostic',
            name='dateProno',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 21, 14, 55, 46, 737612)),
        ),
        migrations.AlterField(
            model_name='shotgun',
            name='dateShotgun',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 21, 14, 55, 46, 735609)),
        ),
        migrations.AlterField(
            model_name='shotgunconfig',
            name='dateCrea',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 21, 14, 55, 46, 735609)),
        ),
    ]
