from django.db import models
from django.db.models.fields import CharField
from django.utils.crypto import get_random_string

from fileinput import filename

import datetime
import os

# Create your models here.

class Commands(models.Model):
    nom = models.CharField(max_length=128, null=False)
    prenom = models.CharField(max_length=128, null=False)
    address = models.CharField(max_length=512, null=False)
    email = models.EmailField(null=False)
    dateLivraison = models.DateTimeField(null=True)
    menu = models.CharField(max_length=256, null=False)
    dateCommandePasse = models.DateTimeField(default= datetime.datetime.now(), blank=True)
    numTel = models.IntegerField(null=True)
    livree = models.BooleanField(default=False, blank=True, null=True)
    link = models.CharField(max_length=64, null=True)
    type = models.CharField(max_length=16, null=True, blank=True)
#     demandePar = models.TextField(null=True, blank=True)
    
#upload_path : chemin d'enregistrement des photos pour l'organigramme
def upload_path(instance, filename):
    return os.path.join(('poles/'+instance.titre+'/'+instance.nom+instance.prenom).encode('ascii', 'ignore').decode('ascii'), filename)

class Pole(models.Model):
    titre = models.CharField(max_length=64, null=False)
    nom = models.CharField(max_length=128, null=False)
    prenom = models.CharField(max_length=128, null=False)
    respo = models.BooleanField(default=False,null=True,blank=True)
    image = models.ImageField(null=True, blank=True, upload_to=upload_path)
    image2 = models.ImageField(null=True, blank=True, upload_to=upload_path)
    texte = models.TextField(null=True, blank=True)
    LienFb = models.CharField(max_length=512, null=True, blank=True)
    LienInsta = models.CharField(max_length=512, null=True, blank=True)
    rang = models.IntegerField(null=True, blank=True,default=13)
    
    
#upload_path_galerie : chemin d'enregistrement des photos pour de la galerie
def upload_path_galerie(instance, filename):
    filebase, extension = filename.split('.')
    name = get_random_string(64)
    return os.path.join(('galerie/images/%s.%s' %(name, extension)).encode('ascii', 'ignore').decode('ascii'))

class Galeriepic(models.Model):
    legende = models.CharField(max_length=64, null=True, blank=True)
    texte = models.TextField(null=True, blank=True)
    image = models.ImageField(null=False, upload_to=upload_path_galerie)
    dateUpload = models.DateTimeField(default= datetime.datetime.now(), blank=True)
    display = models.BooleanField(default=True)
    
class Shotgun(models.Model):
    titre = models.CharField(max_length=512, null=False, blank=False)
    email = models.EmailField(null=False)
    dateShotgun = models.DateTimeField(default= datetime.datetime.now(), blank=True)
    
class ShotgunConfig(models.Model):
    titre = models.CharField(max_length=512, null=False, blank=False)
    nbPlace = models.IntegerField(null=False,blank=True)
    dateDebut = models.DateTimeField(null=True)
    dateFin = models.DateTimeField(null=True)
    dateCrea = models.DateTimeField(default= datetime.datetime.now(), blank=True)
    isActive = models.BooleanField(default=False)
    
class EventQrCode(models.Model):
    link = models.CharField(max_length=256, null=True, blank=True)
    trouve = models.BooleanField(default=False) 
    gagnant = models.BooleanField(null=True,blank=True)
    date = models.DateTimeField(default= datetime.datetime.now(), blank=True)

def upload_imgEquipe(instance, filename):
    filebase, extension = filename.split('.')
    name = get_random_string(64)
    return os.path.join(('pronostic/match/%s.%s' %(name, extension)).encode('ascii', 'ignore').decode('ascii'))

class Match(models.Model):
    equipe1 = models.CharField(null=False, max_length=128)
    equipe2 = models.CharField(null=False,max_length=128)
    imgEquipe1 = models.ImageField(null=True, blank=True, upload_to=upload_imgEquipe)
    imgEquipe2 = models.ImageField(null=True, blank=True, upload_to=upload_imgEquipe)
    dateMatch = models.DateTimeField(null=True)
    cote = models.CharField(null=True,max_length=128)
    resultatEquipe1 = models.IntegerField(null=True)
    resultatEquipe2 = models.IntegerField(null=True)
    gagnantPronostic = models.CharField(null=True, max_length=128)
    isActive = models.BooleanField(default=False)
    isFinish = models.BooleanField(default=False)
    
    
class Pronostic(models.Model):
    email = models.EmailField(null=False)
    nom = models.CharField(null=True,max_length=128)
    prenom = models.CharField(null=True,max_length=128)
    consentement = models.BooleanField(null=False)
    scoreEquipe1 = models.IntegerField(null=True)
    scoreEquipe2 = models.IntegerField(null=True)
    dateProno = models.DateTimeField(default= datetime.datetime.now(), blank=False)
    match = models.ForeignKey(Match, on_delete=models.CASCADE, null=True)
    
    class Meta:
        unique_together=('email','match')
        
class campagneCommande(models.Model):
    nom = models.CharField(max_length=128, null=False)
    prenom = models.CharField(max_length=128, null=False)
    address = models.CharField(max_length=512, null=False)
    email = models.EmailField(null=False)
    dateLivraison = models.DateTimeField(null=True)
    menu = models.CharField(max_length=256, null=False)
    dateCommandePasse = models.DateTimeField(default= datetime.datetime.now(), blank=True)
    numTel = models.IntegerField(null=True)
    livree = models.BooleanField(default=False, blank=True, null=True)
    link = models.CharField(max_length=64, null=True)
    valid = models.BooleanField(default=False)
    demande = models.CharField(max_length=1024,blank=True)
