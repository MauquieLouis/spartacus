from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.http import FileResponse, Http404
from django.http.response import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils import formats
from django.utils import timezone
from django.utils.crypto import get_random_string

from .forms import AddModifyGalerieForm
from .forms import AddModifyPoleForm
from .forms import CommandeDejForm
from .forms import CommandeForm
from .forms import HoraireCommandeForm
from .forms import MatchForm
from .forms import MatchEditForm
from .forms import PronosticForm
from .forms import ShotgunForm
from .forms import ShotgunConfigForm
from .forms import ScanEventForm
from .forms import ScanEvenVerifForm
from .forms import CampagneCommandeForm
from .forms import CampagneCommandeModifyForm

from .models import Commands
from .models import EventQrCode
from .models import Galeriepic
from .models import Match
from .models import Pole
from .models import Pronostic
from .models import campagneCommande

import datetime
from datetime import timedelta
import os

# Create your views here.
def home(request):
    return render(request, 'main/home.html', {'title':'Spartacus'})

def organigramme1(request):
    return render(request, 'main/orga1.html',{'title':'Spartacus - Organigramme'})

def organigrammeV2(request):
    allPoles = Pole.objects.all()
    return render(request, 'main/organigramme2.html',{'title':'Spartacus - OrganigrammeV2', 'poles': allPoles })

def organigrammeV2Effect(request):
    allPoles = Pole.objects.all()
    return render(request, 'main/organigramme2Effect.html',{'title':'Jakitunning Effect', 'poles': allPoles})

def galerie(request):
    allPictures = Galeriepic.objects.all().order_by('dateUpload')
    return render(request, 'main/galerie.html',{'title':'Spartacus - Galerie', 'pictures' : allPictures})

def galerieAfficherImage(request, id):
    picture= get_object_or_404(Galeriepic, pk=id)
    return render(request, 'main/galerie.html',{'title':'Spartacus - Galerie', 'picture' : picture})

def motPoles(request):
    poles = Pole.objects.filter(respo=True).order_by('rang')
    allPoles = Pole.objects.all()
    return render(request, 'main/motPoles.html',{'title':'Spartacus - Mot des pôles', 'poles':poles, 'allPoles':allPoles})

def shotgun(request):
    
    if request.method == 'POST':    #Si appel de la page avec une method POST
        formShotgun = ShotgunForm(request.POST)
        if formShotgun.is_valid():
            formShotgun.save()
            messages.info(request, ('ShotGunReussi'))
            return HttpResponseRedirect(reverse('main:home'))
    else:
        formShotgun = ShotgunForm()
    return render(request, 'main/shotgun.html',{'title':'Spartacus - Shotgun', 'form':formShotgun})

@login_required
def deletePole(request, id):
    pole= get_object_or_404(Pole, pk=id)
    pole.delete()
    messages.info(request, ('Membre supprimé'))
    return HttpResponseRedirect(reverse('main:gestionPoles'))

@login_required
def gestionPoles(request, id=0):
    allPoles = Pole.objects.all().order_by('rang')
    if request.method == 'POST':    #Si appel de la page avec une method POST
        if id != 0:
            pole= get_object_or_404(Pole, pk=id)
            formPole = AddModifyPoleForm(request.POST, request.FILES, instance=pole) 
        else:
            formPole = AddModifyPoleForm(request.POST, request.FILES) 
        if formPole.is_valid():
            formPole.save()
            messages.info(request, ('Changement(s) effectué(s)'))
            return HttpResponseRedirect(reverse('main:gestionPoles'))
    else:
        if id != 0:
            pole = get_object_or_404(Pole, pk=id)
            formPole = AddModifyPoleForm(instance=pole)
        else:
            pole = None
            formPole = AddModifyPoleForm()
    return render(request, 'main/gestionPoles.html', {'title':'Spartacus - Gestion Poles', 'form':formPole, 'poles': allPoles, 'pole':pole})

@login_required
def gestionCommandes(request):
    ttesLesCommandes = Commands.objects.all().order_by('dateLivraison')
    countall = Commands.objects.count()
    countValid = Commands.objects.filter(link="True").count()
    countSoir = Commands.objects.filter(type="soir").count()
    countMatin = Commands.objects.filter(type="matin").count()
    countTarVeg1 = Commands.objects.filter(menu="Tartiflette vegan").count()
    countTarVeg2 = Commands.objects.filter(menu="Tartiflette végétarien").count()
    countTarVeg = countTarVeg1 + countTarVeg2
    countTarLar = Commands.objects.filter(menu = "Tartiflette (lardon porc)").count()
    countTar = Commands.objects.filter(menu = "Tartiflette").count()
    countTarCla = countTar + countTarLar
    countTarHal = Commands.objects.filter(menu = "Tartiflette Halal").count()
    countPDPainMieJo = Commands.objects.filter(menu= "Tranche de pain de mie avec oeufs brouillés/Jus d'orange").count()
    countPDPainMieMt= Commands.objects.filter(menu= "Tranche de pain de mie avec oeufs brouillés/Multifruit").count()
    countPDPainMieCa = Commands.objects.filter(menu= "Tranche de pain de mie avec oeufs brouillés/Café").count()
    countPDPancakeJo = Commands.objects.filter(menu= "Gros pancakes sucrés/Jus d'orange").count()
    countPDPancakeMt = Commands.objects.filter(menu= "Gros pancakes sucrés/Multifruit").count()
    countPDPancakeCa = Commands.objects.filter(menu= "Gros pancakes sucrés/Café").count()
    countPDPainMie = countPDPainMieJo + countPDPainMieMt + countPDPainMieCa
    countPDPancake = countPDPancakeJo + countPDPancakeMt + countPDPancakeCa
    countJusOrange = countPDPancakeJo + countPDPainMieJo
    countMultifruit = countPDPainMieMt + countPDPancakeMt
    countCafe = countPDPancakeCa + countPDPainMieCa
    return render(request, 'main/gestionCommande.html',
                    {'title':'Spartacus - Gestion Commandes',
                    'commandes' : ttesLesCommandes,
                    'count':countall,
                    'countVal':countValid,
                    'countSoir':countSoir,
                    'countMatin':countMatin,
                    'countTarVeg':countTarVeg,
                    'countTarCla':countTarCla,
                    'countTarHal':countTarHal,
                    'countPDPainMie':countPDPainMie,
                    'countPDPancake':countPDPancake,
                    'countJusOrange':countJusOrange,
                    'countMultifruit':countMultifruit,
                    'countCafe':countCafe,
                    #Count Mix
                    'countPDPainMieJo':countPDPainMieJo,
                    'countPDPainMieMt':countPDPainMieMt,
                    'countPDPainMieCa':countPDPainMieCa,
                    'countPDPancakeJo':countPDPancakeJo,
                    'countPDPancakeMt':countPDPancakeMt,
                    'countPDPancakeCa':countPDPancakeCa,
                    })

@login_required
def gestionCommandesInfo(request, command_id):
    commande = Commands.objects.get(pk=command_id)
    return render(request, 'main/gestionCommandeInfo.html', {'title':'Spartacus - Gestion Commandes Infos', 'commande': commande})

@login_required
def deleteCommande(request, command_id):
    commande = Commands.objects.get(pk=command_id)
    numCom = commande.id    
    ownCom = commande.email
    commande.delete()
    messages.info(request, (('La commande n° '+str(numCom)+' de '+ownCom+' à été supprimé')))
    return HttpResponseRedirect(reverse('main:commandeWESGestion'))
   
@login_required
def listePersonnes(request, type):
    commandes = Commands.objects.filter(type=type, link="True").order_by('address')
    return render(request,'main/listePersone.html',{'title':'Spartacus Liste', 'commandes':commandes })
   
@login_required
def configureShotgun(request):
    
    return render(request, 'main/shotgunConfigureForm',{'title':''})
    
@login_required
def validerOuNonCommande(request, command_id):
    commande = Commands.objects.get(pk=command_id)
    if commande.livree == True:
        commande.livree = False
        messages.info(request, ('La commande de %s à été annulé' %commande.email))
    else:
        commande.livree = True
        messages.info(request, ('La commande de %s à été validé' %commande.email))
    commande.save()  
    return HttpResponseRedirect(reverse('main:commandeWESGestion'))

@login_required
def gestionGaleriePicture(request, id=0):
    allPictures = Galeriepic.objects.all().order_by('dateUpload')
    if request.method == 'POST':    #Si appel de la page avec une method POST
        if id != 0:
            picture= get_object_or_404(Galeriepic, pk=id)
            formPic = AddModifyGalerieForm(request.POST, request.FILES, instance=picture) 
        else:
            formPic = AddModifyGalerieForm(request.POST, request.FILES) 
        if formPic.is_valid():
            formPic.save()
            messages.info(request, ('Bien vu !'))
            return HttpResponseRedirect(reverse('main:gestionPictures'))
    else:
        if id != 0:
            picture= get_object_or_404(Galeriepic, pk=id)
            formPic = AddModifyGalerieForm(instance=picture)
        else:
            picture = None
            formPic = AddModifyGalerieForm()
    return render(request, 'main/gestionPicture.html', {'title':'Spartacus - Gestion Galerie', 'form':formPic, 'pictures': allPictures, 'picture':picture})

@login_required
def deletePicture(request, id):
    print("delete")
    picture= get_object_or_404(Galeriepic, pk=id)
    picture.delete()
    messages.info(request, ('Photo supprimée'))
    return HttpResponseRedirect(reverse('main:gestionPictures'))    
    
        
def commandeTypeCorrec(request, typem):
    if request.method == 'POST':
        form = CommandeDejForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            numTel = form.cleaned_data['numTel']
            menu = form.cleaned_data['menu']
            boisson = form.cleaned_data['boisson']
            try:
                commande = Commands.objects.get(email=email,numTel=numTel,type="matin")
            except Commands.DoesNotExist:
                commande = None
                messages.info(request,('Aucune commande avec cet email et ce numéro de Téléphone'))
                return HttpResponseRedirect(reverse('main:commandeWESCorrec',kwargs={'typem': 'matin'}))
#             if '/' in commande.menu:
#                 messages.info(request,('Votre commande est déjà parfaite'))
#                 return HttpResponseRedirect(reverse('main:home'))
            commande.menu = menu+"/"+boisson
            if commande.link=="True":
                send_mail(
                'Spartacus : Re-Validation Commande',
                # ------- / ! \ à changer par spartacus2021.fr
                ('Vos modifications ont été enregistrées'),
                'ne_pas_repondre@spartacus2021.fr',
                [email],
                fail_silently=False,
                )
            else:
                send_mail(
                'Spartacus : Re-Validation Commande',
                # ------- / ! \ à changer par spartacus2021.fr
                ('Vos modifications ont été enregistrées, Cependant vous n\'avez toujours pas validé votre commande, c\'est pas bien'),
                'ne_pas_repondre@spartacus2021.fr',
                [email],
                fail_silently=False,
            )
            commande.save()
            
            messages.info(request,('Modifications enregistrées'))
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = CommandeDejForm()
    return render(request, 'main/formulaireCommandeCorrec.html',{'title' : 'Spartacus - Commande','form':form})
        
def commandeTypeHorraire(request, typem):
    dateActuelle = datetime.datetime.now()
    #Date Fermeture
    if dateActuelle > datetime.datetime.strptime('2021-03-14 21:00:00','%Y-%m-%d %H:%M:%S'):
        messages.info(request, ('Les commandes WES ne sont plus ouvertes.'))
        return HttpResponseRedirect(reverse('main:home'))
    if request.method == 'POST':
        form = HoraireCommandeForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            numTel = form.cleaned_data['numTel']
            horaire = form.cleaned_data['heureLivraison']
            try:
                commande = Commands.objects.get(email=email,numTel=numTel,type="matin")
            except Commands.DoesNotExist:
                commande = None
                messages.info(request,('Aucune commande avec cet email et ce numéro de Téléphone'))
                return HttpResponseRedirect(reverse('main:commandeWESCorrec',kwargs={'typem': 'matin'}))
            dateTimeLivraison = makeDateTime(horaire, '2021-03-15')
            commande.dateLivraison = dateTimeLivraison
            if commande.link=="True":
                send_mail(
                'Spartacus : Re-Validation Commande',
                # ------- / ! \ à changer par spartacus2021.fr
                ('Votre changement d\'horaire est validé'),
                'ne_pas_repondre@spartacus2021.fr',
                [email],
                fail_silently=False,
                )
            else:
                send_mail(
                'Spartacus : Re-Validation Commande',
                # ------- / ! \ à changer par spartacus2021.fr
                ('Votre changement d\'horaire est validé, Cependant vous n\'avez toujours pas validé votre commande, c\'est pas bien'),
                'ne_pas_repondre@spartacus2021.fr',
                [email],
                fail_silently=False,
            )
            commande.save()
            messages.info(request,('Modifications enregistrées'))
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = HoraireCommandeForm()
    return render(request, 'main/formulaireCommandeHorraire.html',{'title' : 'Spartacus - Commande','form':form})        
        
def commandeType(request, typem):

    dateActuelle = datetime.datetime.now()
    #Date ouverture des commandes
    if dateActuelle < datetime.datetime.strptime('2021-03-13 17:00:00','%Y-%m-%d %H:%M:%S'):
                messages.info(request, ('Les commandes WES ne sont pas encore disponibles. Elles ouvrent le 13 mars à 18h00.'))
                return HttpResponseRedirect(reverse('main:home'))
    #Date limite ouverture petit déjeuner
    if dateActuelle > datetime.datetime.strptime('2021-03-14 21:00:00','%Y-%m-%d %H:%M:%S'):
                messages.info(request, ('Les commandes WES ne sont plus ouvertes.'))
                return HttpResponseRedirect(reverse('main:home'))
    if typem == 'soir':
    #Date limite ouverture tartiflette
        if dateActuelle > datetime.datetime.strptime('2021-03-14 15:00:00','%Y-%m-%d %H:%M:%S'):
            messages.info(request, ('Les commandes de tartiflettes sont fermées'))
            return HttpResponseRedirect(reverse('main:commandeWES', kwargs={'typem': 'matin'}))
    if request.method == 'POST':    #Si appel de la page avec une method POST
        formNewCommande = CommandeForm(request.POST, typem=typem) 
        print(formNewCommande.is_valid(), formNewCommande.errors)
        if formNewCommande.is_valid():
            nom = formNewCommande.cleaned_data['nom']
            prenom = formNewCommande.cleaned_data['prenom']
            address = formNewCommande.cleaned_data['address']
            email = formNewCommande.cleaned_data['email']
            heure = formNewCommande.cleaned_data['heureLivraison']
            menu = formNewCommande.cleaned_data['menu']
            #date = formNewCommande.cleaned_data['dateLivraison']
            numTel = formNewCommande.cleaned_data['numTel']
            dateActuelle = datetime.datetime.now()
            if typem == 'soir':
                dateTimeLivraison = makeDateTime(heure, '2021-03-14')
            elif typem == 'matin':
                dateTimeLivraison = makeDateTime(heure, '2021-03-15')
            commande = Commands.objects.create(nom=nom, prenom=prenom, address=address,email=email)
            if typem=='matin':
                boisson = formNewCommande.cleaned_data['boisson']
                commande.menu = menu+"/"+boisson
            else :
                commande.menu = menu
            commande.numTel = numTel
            
            commande.link = generateLink()
            commande.dateLivraison = dateTimeLivraison
            commande.type = typem
            commande.save()
            send_mail(
                'Spartacus : Validation Commande',
                # ------- / ! \ à changer par spartacus2021.fr
                ('Pour valider votre commande cliquer sur ce lien : http://spartacus2021.fr/link/verif/%s'%commande.link),
                'ne_pas_repondre@spartacus2021.fr',
                [email],
                fail_silently=False,
            )
            messages.info(request, ('Vous allez recevoir un mail à l\'adresse %s pour valider votre commande, date livraison : %s '% (email, dateTimeLivraison)))
            return HttpResponseRedirect(reverse('main:home'))
    else:
        formNewCommande = CommandeForm(typem = typem)
    messages.info(request, ('Les commandes WES se terminent le 14 mars 2021 à 22h00 pour les petits-déjeuner et 16h00 pour les tartiflettes'))
    return render(request, 'main/formulaireCommande.html', {'title':'Spartacus - Commande ', 'form' : formNewCommande, 'typem' : typem })

def verificationLink(request, link):
    commande = get_object_or_404(Commands, link=link)
    commande.link=True
    commande.save()
    messages.info(request, ('Commande validé shef !'))
    return HttpResponseRedirect(reverse('main:home'))


def scanCode(request, link):
    qrCode = get_object_or_404(EventQrCode, link=link)
    if request.method == 'POST':
        form = ScanEvenVerifForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == 'calculatricespartacus':
                request.session['mdptext'] = True
                return HttpResponseRedirect(reverse('main:scanQrCodeVerif',kwargs={'link': link}))
            if form.cleaned_data['password'] == 'pastis': 
                return redirect('https://www.51.fr/home')
            messages.info(request,'Mauvais mot de passe !')
            return HttpResponseRedirect(reverse('main:scanQrCode',kwargs={'link': link}))
    else:
        form = ScanEvenVerifForm()
    return render(request, 'main/scanQrCode/scanQrCode.html',{'title':'Spartacus - Scan QR Code', 'form' : form})

def verifScanCode(request, link):
    qrCode = get_object_or_404(EventQrCode, link=link)
    if not request.session['mdptext']:
        messages.info(request,'Le mdp bg !!')
        return HttpResponseRedirect(reverse('main:scanQrCode',kwargs={'link': link}))
    if request.session['mdptext'] == False:
        messages.info(request,'Le mdp bg !!')
        return HttpResponseRedirect(reverse('main:scanQrCode',kwargs={'link': link}))
    if qrCode.trouve:
        if qrCode.gagnant:
            messages.info(request,'Aïe aïe aïe ... Ce code à déjà été trouvé... Il était gagnant ... Dommage')
        else:
            messages.info(request,'Aïe aïe aïe ... Ce code à déjà été trouvé... Il était perdant')
        return HttpResponseRedirect(reverse('main:home'))#,kwargs={'link': link}))
    gagnant = qrCode.gagnant
    qrCode.trouve = True
    qrCode.save()
    qrCodeGagnant = EventQrCode.objects.filter(gagnant=True).filter(trouve=False).count()
    request.session['mdptext'] = False
    return render(request, 'main/scanQrCode/verifScanQrCode.html',{'title':'Spartacus - Verif Qr Code', 'gagnant':gagnant, 'qrCodeGagnant': qrCodeGagnant})

@login_required
def createScanEvent(request):
    if request.method == 'POST':
        form = ScanEventForm(request.POST)
        if form.is_valid():
            nbCode = form.cleaned_data['nbQrCode']
            nbCodeGagnant = form.cleaned_data['nbQrCodeGagnant']
            count = EventQrCode.objects.all().count()
            if count != 0:
                allQrCode = EventQrCode.objects.all()
                for qrCode in allQrCode:
                    qrCode.delete()
            for i in range(0 ,nbCode):
                link = get_random_string(24)
                qrCode = EventQrCode.objects.create(link=link)
                if i < nbCodeGagnant:
                    qrCode.gagnant = True
                else:
                    qrCode.gagnant = False
                qrCode.save()
                
            messages.info(request,('Les liens sont crées'))
            return HttpResponseRedirect(reverse('main:scanQrCodeShowList'))
    else:
        form = ScanEventForm()
    return render(request,'main/scanQrCode/createScanEvent.html',{'title' : 'Spartacus - Creer Scan Event', 'form':form})

@login_required
def showScanEvent(request):
    listeCode = EventQrCode.objects.all()
    return render(request, 'main/scanQrCode/showScanEvent.html',{'title' : 'Spartacus - Afficher Scan Event', 'listeCode':listeCode})

#=================PRONOSTIC====================#

def listePronostic(request):
    matchs = Match.objects.filter(isActive=False)
    return render(request, 'main/pronostic/listePronostic.html',{'title':'Spartacus - Pronostic', 'matchs':matchs})

def detailPronostic(request, pk):
    match = get_object_or_404(Match, pk=pk)
    countPr = Pronostic.objects.filter(match=match).count()
    if countPr:
        pronostics = Pronostic.objects.filter(match=match).order_by('dateProno')
    else:
        pronostics = None
    return render(request, 'main/pronostic/detailPronostic.html',{'title': 'Spartacus - Pronostic','match':match, 'pronostics':pronostics})

def fairePronostic(request):
    dateActuelle = datetime.datetime.now()
    now = timezone.now()
    print(now)
    formDisable=False
    testActiveMatch = Match.objects.filter(isActive=True).count()
    if testActiveMatch:
        match = Match.objects.get(isActive=True)
        print(match.dateMatch)
        if now+timedelta(hours=2) > match.dateMatch:
            formDisable = True
    else:
        match = None
    if request.method=='POST':  
        if now > match.dateMatch:
            messages.info(request,'Hummm... Malheureusement l\'heure pour faire des pronostics est passée.')
            messages.info(request,'Votre pronostic n\'a pas pu être enregistré.')
            return HttpResponseRedirect(reverse('main:detailPronostic',kwargs={'pk': match.id}))
        form = PronosticForm(request.POST)
        if form.is_valid():
            pronoTest = Pronostic.objects.filter(email=form.cleaned_data['email'],match=match).count()
            if pronoTest:
                messages.info(request,'Un pari avec l\'email '+form.cleaned_data['email']+' à déjà été enregistré pour ce match.')
                print(pronoTest)
                return HttpResponseRedirect(reverse('main:fairePronostic'))
            email = form.cleaned_data['email']
            listInfo = splitEmail(email)
            if not(listInfo[2] == 'telecom-sudparis' or listInfo[2] == 'imt-bs'):
                messages.info(request,'Malheureusement l\'adresse email n\'est pas valide')
                return HttpResponseRedirect(reverse('main:fairePronostic'))
            prono = form.save(commit=False)
            prono.nom = listInfo[1]
            prono.prenom = listInfo[0]
            prono.match = match
            prono.save()
            form.save_m2m()
            messages.info(request,'Pronostic enregistré pour JMLAZONE91')
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = PronosticForm()
    return render(request, 'main/pronostic/fairePronostic.html',{'title':'Spartacus - Pronostic','form':form, 'match':match, 'formDisable':formDisable})

@login_required
def createMatch(request):
    if request.method == 'POST':
        form = MatchForm(request.POST, request.FILES)
        if form.is_valid():
            if form.cleaned_data['isActive'] :
                count = Match.objects.filter(isActive=True).count()
                if count:
                    match = Match.objects.get(isActive=True)
                    match.isActive = False
                    match.save()
            form.save()
            messages.info(request,('Match crée'))
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = MatchForm()
    return render(request,'main/pronostic/createMatch.html',{'title':'Spartacus - Match','form':form})

@login_required
def modifyMatch(request, pk):
    match = get_object_or_404(Match,pk=pk)
    if request.method == 'POST':
        form = MatchEditForm(request.POST, request.FILES,instance = match)
        if form.is_valid():
            if form.cleaned_data['isActive'] :
                count = Match.objects.filter(isActive=True).count()
                if count:
                    match = Match.objects.get(isActive=True)
                    match.isActive = False
                    match.save()
            form.save()
            messages.info(request,('Match modifié'))
            return HttpResponseRedirect(reverse('main:gestionMatch'))
    else:
        form = MatchEditForm(instance = match)
    return render(request,'main/pronostic/editMatch.html',{'title':'Spartacus - Match','form':form, 'match':match})

@login_required
def gestionMatch(request):
    testActiveMatch = Match.objects.filter(isActive=True).count()
    if testActiveMatch:
        activeMatch = Match.objects.get(isActive=True)
    else:
        activeMatch = None
    otherMatch = Match.objects.filter(isActive=False)
    print(activeMatch, otherMatch)
    return render(request, 'main/pronostic/gestionMatch.html',{'title':'Spartacus - Match', 'activeMatch':activeMatch,'otherMatch':otherMatch})

@login_required
def deleteMatch(request, pk):
    match = get_object_or_404(Match, pk=pk)
    match.delete()
    messages.info(request,('Match supprimé'))
    return HttpResponseRedirect(reverse('main:gestionMatch'))

def pdfView(request):
    try:
        return FileResponse(open('/home/spartacus/spartacus/main/static/presentation.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def commandeCampagneType(request):
    dateActuelle = datetime.datetime.now()
    #Date ouverture des commandes
#     if dateActuelle < datetime.datetime.strptime('2021-03-13 17:00:00','%Y-%m-%d %H:%M:%S'):
#                 messages.info(request, ('Les commandes WES ne sont pas encore disponibles. Elles ouvrent le 13 mars à 18h00.'))
#                 return HttpResponseRedirect(reverse('main:home'))
#     #Date limite ouverture petit déjeuner
    if dateActuelle > datetime.datetime.strptime('2021-05-03 16:00:00','%Y-%m-%d %H:%M:%S'):
                messages.info(request, ('Les commandes de petit-déjeuner pour la campagne ne sont plus ouvertes.'))
                return HttpResponseRedirect(reverse('main:home'))
    if request.method == 'POST':    #Si appel de la page avec une method POST
        formNewCommande = CampagneCommandeForm(request.POST) 
        print(formNewCommande.is_valid(), formNewCommande.errors)
        if formNewCommande.is_valid():
            nom = formNewCommande.cleaned_data['nom']
            prenom = formNewCommande.cleaned_data['prenom']
            address = formNewCommande.cleaned_data['address']
            email = formNewCommande.cleaned_data['email']
            heure = formNewCommande.cleaned_data['heureLivraison']
            menu = formNewCommande.cleaned_data['menu']
            numTel = formNewCommande.cleaned_data['numTel']
            dateActuelle = datetime.datetime.now()
            dateTimeLivraison = makeDateTime(heure,'2021-05-04')
            commande = campagneCommande.objects.create(nom=nom, prenom=prenom, address=address,email=email)
            #boisson = formNewCommande.cleaned_data['boisson']
            commande.menu = menu#+"/"+boisson
            commande.numTel = numTel
            commande.link = generateLink()
            commande.dateLivraison = dateTimeLivraison
            commande.demande = formNewCommande.cleaned_data['demande']
            commande.save()
            send_mail(
                'Spartacus : Validation Commande',
                ('Nous avons bien reçu votre commande, merci de la valider avec le lien suivant : http://spartacus2021.fr/link/verif/%s'%commande.link),
                'ne_pas_repondre@spartacus2021.fr',
                [email],
                fail_silently=False,
            )
            messages.info(request, ('Vous allez recevoir un mail à l\'adresse %s pour valider votre commande, date livraison : %s '% (email, dateTimeLivraison)))
            return HttpResponseRedirect(reverse('main:home'))
    else:
        formNewCommande = CampagneCommandeForm()
    return render(request, 'main/campagne/formulaireCampagneCommande.html', {'title':'Spartacus - Campagne commande ', 'form' : formNewCommande, })

def verificationLink(request, link):
    commande = get_object_or_404(campagneCommande, link=link)
    if commande.valid == True:
        messages.info(request, ('%s ta commande est déjà validée !!!  Livraison le : %s '% (commande.prenom, formats.date_format(commande.dateLivraison,"SHORT_DATETIME_FORMAT"))))
        return HttpResponseRedirect(reverse('main:home'))
    commande.valid=True
    commande.save()
    messages.info(request, ('Commande validé shef !'))
    return HttpResponseRedirect(reverse('main:home'))

@login_required
def listeCampagneCommande(request):
    countCommande = campagneCommande.objects.filter(valid=True).count()
    countNonValid = campagneCommande.objects.filter(valid=False).count()
    countSale = campagneCommande.objects.filter(menu="Menu salé").count()
    countSucre = campagneCommande.objects.filter(menu="Menu sucré").count()
    countTotal = countCommande + countNonValid
    commandes = campagneCommande.objects.filter(valid=True).order_by('dateLivraison')
    return render(request, 'main/campagne/listeCommande.html',
                  {'title':'Spartacus - Campagne Liste Commande',
                    'count':countCommande, 'commandes':commandes,
                    'countCommande':countCommande,
                    'countNonValid':countNonValid,
                    'countTotal':countTotal,
                    'countSale':countSale,
                    'countSucre':countSucre,
                    })
 
@login_required
def changementCommande(request, pk):
    commande = campagneCommande.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = CampagneCommandeModifyForm(request.POST) 
        if form.is_valid():
            dateTimeLivraison = makeDateTime(form.cleaned_data['heureLivraison'],'2021-05-04')
            commande.dateLivraison = dateTimeLivraison
            commande.save()
            messages.info(request,('C\'est changé'))
            return HttpResponseRedirect(reverse('main:home'))
    else:
        form = CampagneCommandeModifyForm() 
    return render(request,'main/campagne/changementCommande.html',{'title':'Spartacus changement Commande','form':form, 'nom':commande.nom, 'prenom':commande.prenom})

@login_required
def deleteCampagneCommande(request, pk):
    commande = campagneCommande.objects.get(pk=pk)
    commande.delete()
    messages.info(request,('supprimé'))
    return HttpResponseRedirect(reverse('main:home'))

@login_required
def listNonValid(request):
    countCommande = campagneCommande.objects.filter(valid=True).count()
    countNonValid = campagneCommande.objects.filter(valid=False).count()
    countSale = campagneCommande.objects.filter(menu="Menu salé").count()
    countSucre = campagneCommande.objects.filter(menu="Menu sucré").count()
    countTotal = countCommande + countNonValid
    commandes = campagneCommande.objects.filter(valid=False).order_by('dateLivraison')
    return render(request, 'main/campagne/listeCommande.html',
                  {'title':'Spartacus - Campagne Liste Commande',
                    'count':countCommande, 'commandes':commandes,
                    'countCommande':countCommande,
                    'countNonValid':countNonValid,
                    'countTotal':countTotal,
                    'countSale':countSale,
                    'countSucre':countSucre,
                    })
    
#-----------------------------------------------------------------------------#
#                          PAS LES VUES                                       #
#-----------------------------------------------------------------------------#

def generateLink():
    link = get_random_string(64)
    return link

def makeDateTime(heure, date):
    tablHeure=heure.split('h')
    date_time_str = date+' '+tablHeure[0]+':'+tablHeure[1]+':00'
    date_time_obj = datetime.datetime.strptime(date_time_str,'%Y-%m-%d %H:%M:%S')
    return date_time_obj

def splitEmail(email):
    emailSplit = email.split('@')
    if '.' in emailSplit[0]:
        nomPrenom = emailSplit[0].split('.')
    else:
        nomPrenom = [emailSplit[0], 'Jakitunning']
    address = emailSplit[1].split('.')
    return [nomPrenom[0], nomPrenom[1], address[0]]
    
    
