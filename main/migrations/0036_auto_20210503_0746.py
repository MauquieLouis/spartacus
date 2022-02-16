# Generated by Django 3.1.5 on 2021-05-03 05:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0035_auto_20210502_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='campagnecommande',
            name='demande',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='campagnecommande',
            name='dateCommandePasse',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 3, 7, 46, 52, 51486)),
        ),
        migrations.AlterField(
            model_name='commands',
            name='dateCommandePasse',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 3, 7, 46, 52, 47521)),
        ),
        migrations.AlterField(
            model_name='eventqrcode',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 3, 7, 46, 52, 49521)),
        ),
        migrations.AlterField(
            model_name='galeriepic',
            name='dateUpload',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 3, 7, 46, 52, 48524)),
        ),
        migrations.AlterField(
            model_name='pronostic',
            name='dateProno',
            field=models.DateTimeField(default=datetime.datetime(2021, 5, 3, 7, 46, 52, 50495)),
        ),
        migrations.AlterField(
            model_name='shotgun',
            name='dateShotgun',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 3, 7, 46, 52, 48524)),
        ),
        migrations.AlterField(
            model_name='shotgunconfig',
            name='dateCrea',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 5, 3, 7, 46, 52, 49521)),
        ),
    ]