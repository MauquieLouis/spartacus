# Generated by Django 3.1.5 on 2021-02-22 18:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210222_1153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commands',
            name='dateCommandePasse',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 22, 19, 17, 45, 406056)),
        ),
        migrations.AlterField(
            model_name='pole',
            name='image',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
        migrations.AlterField(
            model_name='pole',
            name='image2',
            field=models.CharField(blank=True, max_length=512, null=True),
        ),
    ]
