# Generated by Django 3.1.5 on 2021-04-19 11:45

import datetime
from django.db import migrations, models
import django.db.models.deletion
import main.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20210328_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipe1', models.CharField(max_length=128)),
                ('equipe2', models.CharField(max_length=128)),
                ('imgEquipe1', models.ImageField(blank=True, null=True, upload_to=main.models.upload_imgEquipe)),
                ('imgEquipe2', models.ImageField(blank=True, null=True, upload_to=main.models.upload_imgEquipe)),
                ('dateMatch', models.DateField(null=True)),
                ('cote', models.CharField(max_length=128, null=True)),
                ('resultat', models.CharField(max_length=128, null=True)),
                ('gagnantPronostic', models.CharField(max_length=128, null=True)),
                ('isActive', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='commands',
            name='dateCommandePasse',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 13, 45, 49, 94476)),
        ),
        migrations.AlterField(
            model_name='eventqrcode',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 13, 45, 49, 97467)),
        ),
        migrations.AlterField(
            model_name='galeriepic',
            name='dateUpload',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 13, 45, 49, 95473)),
        ),
        migrations.AlterField(
            model_name='shotgun',
            name='dateShotgun',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 13, 45, 49, 96468)),
        ),
        migrations.AlterField(
            model_name='shotgunconfig',
            name='dateCrea',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 19, 13, 45, 49, 96468)),
        ),
        migrations.CreateModel(
            name='Pronostic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('nom', models.CharField(max_length=128, null=True)),
                ('prenom', models.CharField(max_length=128, null=True)),
                ('consentement', models.BooleanField(default=False)),
                ('scoreEquipe1', models.IntegerField(null=True)),
                ('scoreEquipe2', models.IntegerField(null=True)),
                ('dateProno', models.DateTimeField(default=datetime.datetime(2021, 4, 19, 13, 45, 49, 97467))),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.match')),
            ],
        ),
    ]
