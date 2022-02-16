# Generated by Django 3.1.5 on 2021-02-22 10:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20210219_0111'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pole',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=64)),
                ('nom', models.CharField(max_length=128)),
                ('prenom', models.CharField(max_length=128)),
                ('respo', models.BooleanField(blank=True, default=False, null=True)),
                ('image', models.CharField(max_length=256, null=True)),
                ('image2', models.CharField(max_length=256, null=True)),
                ('texte', models.TextField(blank=True, null=True)),
                ('LienFb', models.CharField(max_length=512, null=True)),
                ('LienInsta', models.CharField(max_length=512, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='commands',
            name='dateCommandePasse',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 2, 22, 11, 8, 40, 262355)),
        ),
    ]