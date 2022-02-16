from django import forms
from django.forms.widgets import Select

from .models import Pole, Shotgun, ShotgunConfig
from .models import Galeriepic, Pronostic, Match
from .models import campagneCommande

class CommandeDejForm(forms.Form):
    email = forms.EmailField(label='Entrer le mail avec lequel vous avez passé la commande')
    numTel = forms.IntegerField(label='Entrer le numéro de téléphone')
    menu = forms.ChoiceField(widget=forms.RadioSelect, choices=[('Tranche de pain de mie avec oeufs brouillés','Tranche de pain de mie avec oeufs brouillés'),('Gros pancakes sucrés','Gros pancakes sucrés')])
    boisson = forms.ChoiceField(widget=forms.RadioSelect, choices=[('Jus d\'orange','Jus d\'orange'),('MultiFruit','MultiFruit'),('Café','Café')])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'id':'email',
                                                      'placeholder':'Entrer le mail avec lequel vous avez passé la commande',
                                                      'class': 'form-control',
                                                      })
        self.fields['numTel'].widget.attrs.update({'id':'numTel',
                                                      'placeholder':'Entrer le numéro de Tél. avec lequel vous avez passé la commande',
                                                      'class': 'form-control',
                                                      })
        self.fields['menu'].widget.attrs.update({'id':'menu',
                                                      'placeholder':'Entrer le numéro de Tél. avec lequel vous avez passé la commande',
                                                      'class': 'form-check-input form-check-inline',
                                                      })
        
class HoraireCommandeForm(forms.Form):
    email = forms.EmailField(label='Entrer le mail avec lequel vous avez passé la commande')
    numTel = forms.IntegerField(label='Entrer le numéro de téléphone')
    heureLivraison = forms.ChoiceField(widget=forms.Select(),help_text="Délai de livraison de 15min", choices=[('Error','Error')])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'id':'email',
                                                      'placeholder':'Entrer le mail avec lequel vous avez passé la commande',
                                                      'class': 'form-control',
                                                      })
        self.fields['numTel'].widget.attrs.update({'id':'numTel',
                                                      'placeholder':'Entrer le numéro de Tél. avec lequel vous avez passé la commande',
                                                      'class': 'form-control',
                                                      })
        self.fields['heureLivraison'].widget.attrs.update({'id':'heureLivraison',
                                                      'placeholder':'Choisir l\'horaire de livraison',
                                                      'class': 'form-control form-control-sm',
                                                      })
        self.fields['heureLivraison'].choices=[
                ('8h30', '8h30'),
                ('9h00', '9h'),
                ('9h30', '9h30'),
                ('10h00', '10h'),
                ('10h30', '10h30'),
                ('11h00', '11h'),
                ('11h30', '11h30'),
                ('12h00', '12h'),
                ]
        
class CommandeForm(forms.Form):
    nom = forms.CharField(label='Entrer un nom', max_length=127)
    prenom = forms.CharField(label='Entrer un prenom', max_length=127)
    address = forms.CharField(label='Entrer un nom', max_length=512)
    email = forms.EmailField(label='Entrer un email')
    #dateLivraison = forms.DateField(widget=forms.SelectDateWidget(years=range(2021,2022)))#widget=forms.DateTimeInput)
    #demandePar = forms.CharField(label="Demande particulière")
    heureLivraison = forms.ChoiceField(widget=forms.Select(),help_text="Délai de livraison de 15min", choices=[('Error','Error')])
    menu = forms.ChoiceField(widget=forms.RadioSelect(), choices=[('Error','Error')]) #choices=[('Menu 1','Menu 1'),('Menu 2','Menu 2'),('Menu 3','Menu 3')])
    boisson = forms.ChoiceField(widget=forms.RadioSelect(),choices=[('Error','Error')])
    numTel = forms.IntegerField()
    def __init__(self, *args, **kwargs):
        typem = kwargs.pop("typem")
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'id':'nom',
                                                      'placeholder':'Entrer un nom',
                                                      'class': 'form-control',
                                                      })
        self.fields['prenom'].widget.attrs.update({'id':'prenom',
                                                      'placeholder' : 'Entrer un prénom',
                                                      'class': 'form-control',
                                                      })
        self.fields['address'].widget.attrs.update({'id':'address',
                                                      'placeholder' : 'Numéro de chambre',
                                                      'class': 'form-control',
                                                      })
        self.fields['email'].widget.attrs.update({'id':'email',
                                                      'placeholder' : 'Entrer une adresse email',
                                                      'class': 'form-control',
                                                      })
#         self.fields['dateLivraison'].widget.attrs.update({'id':'dateLivraison',
#                                                       'class': 'form-control form-control-sm',
#                                                       'style':'width: 33%; display: inline-block;',
#                                                       })
        self.fields['heureLivraison'].widget.attrs.update({'id':'heureLivraison',
                                                      'class': 'form-control form-control-sm',
                                                      'style':'',
                                                      })
        self.fields['menu'].widget.attrs.update({'id':'menu',
                                                      'class': 'form-check-input form-check-inline',
                                                      })
        self.fields['boisson'].widget.attrs.update({'id':'boisson',
                                                      'class': 'form-check-input form-check-inline',
                                                      })
        self.fields['boisson'].required=False
        self.fields['numTel'].widget.attrs.update({'id':'numTel',
                                                      'placeholder':'Entrer un numéro de téléphone',
                                                      'class': 'form-control form-control-sm',
                                                      })
#         self.fields['demandePar'].widget.attrs.update({'id':'demandePar',
#                                                       'placeholder':'Demande particulière',
#                                                       'class': 'form-control form-control-sm',
#                                                       })
# ------------------------------------------------------ #
#                    M I D I                             #
# ------------------------------------------------------ #        

# ------------------------------------------------------ #
#                    S O I R                             #
# ------------------------------------------------------ #            
        if (typem =="soir"):
            self.fields['heureLivraison'].choices=[
                ('18h00', '18h'),
                ('18h30', '18h30'),
                ('19h00', '19h'),
                ('19h30', '19h30'),
                ('20h00', '20h'),
                ('20h30', '20h30'),
                ('21h00', '21h'),
                ('21h30', '21h30'),
                ('22h00', '22h'),
                ]
            self.fields['menu'].choices=[
                ('Tartiflette (lardon porc)','Tartiflette (lardon porc)'),('Tartiflette végétarien', 'Tartiflette végétarien'),('Tartiflette Halal','Tartiflette Halal')
                ]
            self.fields['boisson'].widget.attrs.update({'style':'display:none'})
            self.fields['boisson'].choices=[
                ('','')
                ]
# ------------------------------------------------------ #
#                    M A T I N                           #
# ------------------------------------------------------ # 
        if (typem =="matin"):
            
            self.fields['heureLivraison'].choices=[
                ('8h30', '8h30'),
                ('9h00', '9h'),
                ('9h30', '9h30'),
                ('10h00', '10h'),
                ('10h30', '10h30'),
                ('11h00', '11h'),
                ('11h30', '11h30'),
                ('12h00', '12h'),
                ]
            self.fields['menu'].choices=[
                ('Tranche de pain de mie avec oeufs brouillés','Tranche de pain de mie avec oeufs brouillés'),
                ('Gros pancakes sucrés','Gros pancakes sucrés')
                ]
            self.fields['boisson'].choices=[
                ('Jus d\'orange','Jus d\'orange'),
                ('Multifruit','Multifruit'),
                ('Café','Café'),
                ]
class CampagneCommandeModifyForm(forms.Form):
    heureLivraison = forms.ChoiceField(label="Choisir l'horaire de livraison :",widget=forms.Select(),help_text="Délai de livraison de 15min", choices=[('Error','Error')])
    menu = forms.ChoiceField(widget=forms.RadioSelect(), choices=[('Menu sucré','Menu sucré'),('Menu salé','Menu salé')])
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['heureLivraison'].widget.attrs.update({'id':'heureLivraison',
                                                      'class': 'form-control form-control-sm',
                                                      'style':'',
                                                      })
        self.fields['menu'].widget.attrs.update({'id':'menu',
                                                      'class': 'form-check-input form-check-inline',
                                                      })
        self.fields['menu'].required=False
        self.fields['heureLivraison'].required=False
        self.fields['heureLivraison'].choices=[
                ('9h00', '9h'),
                ('9h30', '9h30'),
                ('10h00', '10h'),
                ('10h30', '10h30'),
                ('11h00', '11h'),
                ('11h30', '11h30'),
                ('12h00', '12h'),
                ('12h30', '12h30'),
                ('13h00', '13h'),
                ('13h30', '13h30'),
                ('14h00', '14h'),
                ('14h30', '14h30'),
                ('15h00', '15h'),
                ('15h30', '15h30'),
                ('16h00', '16h'),
                ('16h30', '16h30'),
                ('17h00', '17h'),
                ('17h30', '17h30'),
                ('18h00', '18h'),
                ]
class CampagneCommandeForm(forms.Form):
    nom = forms.CharField(label='Nom :', max_length=127)
    prenom = forms.CharField(label='Prénom :', max_length=127)
    address = forms.CharField(label='Numéro de chambre ou adresse :', max_length=512)
    email = forms.EmailField(label='Email :')
    heureLivraison = forms.ChoiceField(label="Choisir l'horaire de livraison :",widget=forms.Select(),help_text="Délai de livraison de 15min", choices=[('Error','Error')])
    menu = forms.ChoiceField(label="Choisir à manger :",widget=forms.RadioSelect(), choices=[('Menu sucré','Menu sucré'),('Menu salé','Menu salé')]) #choices=[('Menu 1','Menu 1'),('Menu 2','Menu 2'),('Menu 3','Menu 3')])
#     boisson = forms.ChoiceField(label="Choisir à boire :",widget=forms.RadioSelect(),choices=[('Error','Error')])
    numTel = forms.IntegerField(label="Numéro de Téléphone : ")
    demande = forms.CharField(label="Demande particulière, pas de smiley sinon ca marche pas", max_length=1024)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'id':'nom',
                                                      'placeholder':'Entrer un nom',
                                                      'class': 'form-control',
                                                      })
        self.fields['prenom'].widget.attrs.update({'id':'prenom',
                                                      'placeholder' : 'Entrer un prénom',
                                                      'class': 'form-control',
                                                      })
        self.fields['address'].widget.attrs.update({'id':'address',
                                                      'placeholder' : 'Entrer un Numéro de chambre, ou votre adresse',
                                                      'class': 'form-control',
                                                      })
        self.fields['email'].widget.attrs.update({'id':'email',
                                                      'placeholder' : 'Entrer une adresse email',
                                                      'class': 'form-control',
                                                      })
#         self.fields['dateLivraison'].widget.attrs.update({'id':'dateLivraison',
#                                                       'class': 'form-control form-control-sm',
#                                                       'style':'width: 33%; display: inline-block;',
#                                                       })
        self.fields['heureLivraison'].widget.attrs.update({'id':'heureLivraison',
                                                      'class': 'form-control form-control-sm',
                                                      'style':'',
                                                      })
        self.fields['menu'].widget.attrs.update({'id':'menu',
                                                      'class': 'form-check-input form-check-inline',
                                                      })
#         self.fields['boisson'].widget.attrs.update({'id':'boisson',
#                                                       'class': 'form-check-input form-check-inline',
#                                                       })
        self.fields['demande'].widget.attrs.update({'id':'demande',
                                                      'class': 'form-control form-control-sm',
                                                      'placeholder':'Demande particulière, pas de smiley sinon ca marche pas',
                                                      })
#         self.fields['boisson'].required=False
        self.fields['demande'].required=False
        self.fields['numTel'].widget.attrs.update({'id':'numTel',
                                                      'placeholder':'Entrer un numéro de téléphone',
                                                      'class': 'form-control form-control-sm',
                                                      })
        self.fields['heureLivraison'].choices=[
                ('9h00', '9h'),
                ('9h30', '9h30'),
                ('10h00', '10h'),
                ('10h30', '10h30'),
                ('11h00', '11h'),
                ('11h30', '11h30'),
                ('12h00', '12h'),
                ('12h30', '12h30'),
                ('13h00', '13h'),
                ('13h30', '13h30'),
                ('14h00', '14h'),
                ('14h30', '14h30'),
                ('15h00', '15h'),
                ('15h30', '15h30'),
                ('16h00', '16h'),
                ('16h30', '16h30'),
                ('17h00', '17h'),
                ('17h30', '17h30'),
                ('18h00', '18h'),
                ]
        
class AddModifyPoleForm(forms.ModelForm):#forms.Form):
    class Meta:
        model = Pole
        fields =("titre","nom","prenom","respo","image","image2","texte","LienFb","LienInsta","rang")
        widgets = { 'titre' : Select(choices=[
            ('Sélectionner un pôle','Sélectionner un pôle'),
            ('Président', 'Président'),
            ('VP TSP', 'VP TSP'),
            ('VP IMT-BS', 'VP IMT-BS'),
            ('VP Bachelor', 'VP Bachelor'),
            ('Secrétariat', 'Secrétariat'),
            ('Trésorie', 'Trésorie'),
            ('Trésorerie', 'Trésorerie'),
            ('Relations entreprises', 'Relations entreprises'),
            ('Soirée', 'Soirée'),
            ('Communication', 'Communication'),
            ('Prévention', 'Prévention'),
            ('Sécu-log', 'Sécu-log'),
            ('SWEI-WES-WEA', 'SWEI-WES-WEA'),
            ('Stand', 'Stand'),
            ('DD', 'DD'),
            ('Web', 'Web'),
            ]),
            'rang' : Select(choices=[
                (0,0),
                (1,1),
                (2,2),
                (3,3),
                (4,4),
                (5,5),
                (6,6),
                (7,7),
                (8,8),
                (9,9),
                (10,10),
                (11,11),
                (12,12),
                (13,13),
                ])
                }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nom'].widget.attrs.update({'id':'nom',
                                                  'placeholder':'Entrer un nom',
                                                  'class': 'form-control',
                                                  })
        self.fields['prenom'].widget.attrs.update({'id':'prenom',
                                                  'placeholder':'Entrer un prenom',
                                                  'class': 'form-control',
                                                  })
        self.fields['titre'].widget.attrs.update({'id':'titre',
                                                  'placeholder':'Entrer le nom du pole (première lettre en majuscule, et sans accent)',
                                                  'class': 'form-control',
                                                  })
        self.fields['respo'].widget.attrs.update({'id':'respo',
                                                  'placeholder':'',
                                                  'class': 'form-control',
                                                  })
        self.fields['image'].widget.attrs.update({'id':'image',
                                                  'placeholder':'Choisir la 1ère image',
                                                  'class': 'form-control-file',
                                                  })
        self.fields['image2'].widget.attrs.update({'id':'image2',
                                                  'placeholder':'Choisir la 2ème image',
                                                  'class': 'form-control-file',
                                                  })
        self.fields['texte'].widget.attrs.update({'id':'texte',
                                                  'placeholder':'Entrer le "mot du pôle"',
                                                  'class': 'form-control',
                                                  })
        self.fields['LienFb'].widget.attrs.update({'id':'LienFb',
                                                  'placeholder':'Entrer le lien facebook',
                                                  'class': 'form-control',
                                                  })
        self.fields['LienInsta'].widget.attrs.update({'id':'LienInsta',
                                                  'placeholder':'Entrer le lien Instagram',
                                                  'class': 'form-control',
                                                  })
        self.fields['rang'].widget.attrs.update({'id':'rang',
                                                  'placeholder':'',
                                                  'class': 'form-control',
                                                  })
        
        
class AddModifyGalerieForm(forms.ModelForm):#
    class Meta:
        model = Galeriepic
        fields =("legende", "texte", "image", "display")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['legende'].widget.attrs.update({'id':'legende',
                                              'placeholder':'Entrer une éventuelle légende pour la photo',
                                              'class': 'form-control',
                                              })
        self.fields['texte'].widget.attrs.update({'id':'texte',
                                              'placeholder':'Entrer un éventuel texte de description pour la photo',
                                              'class': 'form-control',
                                              })
        self.fields['image'].widget.attrs.update({'id':'image',
                                                  'placeholder':'Choisir l\'image',
                                                  'class': 'form-control-file',
                                                  })
        self.fields['display'].widget.attrs.update({'id':'display',
                                                  'placeholder':'',
                                                  'class': 'form-check-input',
                                                  })
        
        
class ShotgunForm(forms.ModelForm):
    class Meta:
        model = Shotgun
        fields = ("email",)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'id':'email',
                                              'placeholder':'Entrer votre adresse email',
                                              'class': 'form-control',
                                              })
class ShotgunConfigForm(forms.ModelForm):
    class Meta:
        model = ShotgunConfig
        fields = ("titre",)
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['titre'].widget.attrs.update({'id':'titre',
                                              'placeholder':'Entrer un titre pour le shotgun',
                                              'class': 'form-control',
                                              })
        
class ScanEventForm(forms.Form):
    nbQrCode = forms.IntegerField(label='Entrer le nombre de QR Code')
    nbQrCodeGagnant = forms.IntegerField(label='Entrer le nombre de QR Code Gagnant')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nbQrCode'].widget.attrs.update({'id':'nbQrCode',
                                              'placeholder':'Entrer le nombre de QR Code',
                                              'class': 'form-control',
                                              })
        self.fields['nbQrCodeGagnant'].widget.attrs.update({'id':'nbQrCodeGagnant',
                                              'placeholder':'Entrer le nombre de QR Code Gagnant',
                                              'class': 'form-control',
                                              })
class ScanEvenVerifForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password'].widget.attrs.update({'id':'password',
                                              'placeholder':'Et alors ! le mdp c\'est "pastis" ',
                                              'class': 'form-control',
                                              })

class PronosticForm(forms.ModelForm):
    class Meta:
        model = Pronostic
        fields =("email","scoreEquipe1","scoreEquipe2","consentement")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['consentement'].required = True
        self.fields['email'].widget.attrs.update({'id':'email',
                                              'placeholder':'Email TSP ou IMTBS',
                                              'class': 'form-control',
                                              })
        self.fields['scoreEquipe1'].widget.attrs.update({'id':'scoreEquipe1',
                                              'placeholder':'Entrer le score pour cette équipe',
                                              'class': 'form-control',
                                              })
        self.fields['scoreEquipe2'].widget.attrs.update({'id':'scoreEquipe2',
                                              'placeholder':'Entrer le score pour cette équipe',
                                              'class': 'form-control',
                                              })
        self.fields['consentement'].widget.attrs.update({'id':'consentement',
                                              'placeholder':'J\'accepte que mon nom, prénom et mon pronostic soient diffusés',
                                              'label':'J\'accepte que mon nom, prénom et mon pronostic soient diffusés',
                                              'class': 'form-check-input',
                                              })

class MatchForm(forms.ModelForm):
    class Meta:
        model = Match
        fields =("equipe1","imgEquipe1","equipe2","imgEquipe2","dateMatch","isActive")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['equipe1'].widget.attrs.update({'id':'equipe1',
                                              'placeholder':'Nom de l\'équipe n°1',
                                              'class': 'form-control',
                                              })
        self.fields['equipe2'].widget.attrs.update({'id':'equipe2',
                                              'placeholder':'Nom de l\'équipe n°2',
                                              'class': 'form-control',
                                              })
        self.fields['imgEquipe2'].widget.attrs.update({'id':'imgEquipe2',
                                              'placeholder':'Image équipe 2',
                                              'class': 'form-control-file',
                                              })
        self.fields['imgEquipe1'].widget.attrs.update({'id':'imgEquipe1',
                                              'placeholder':'Image équipe 1',
                                              'class': 'form-control-file',
                                              })
        self.fields['dateMatch'].widget.attrs.update({'id':'dateMatch',
                                              'placeholder':'Date du Match',
                                              'class': 'form-control',
                                              'type':'datetime-local',
                                              })
        self.fields['isActive'].widget.attrs.update({'id':'isActive',
                                              'placeholder':'Est-ce le prochain match ou y en a-t-il un avant ? (si oui cocher)',
                                              'label':'Est-ce le prochain match ou y en a-t-il un avant ? (si oui cocher)',
                                              'class': 'form-check-input',
                                              })

class MatchEditForm(forms.ModelForm):
    class Meta:
        model = Match
        fields = ("isActive","resultatEquipe1","resultatEquipe2","isFinish")
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['isActive'].widget.attrs.update({'id':'isActive',
                                              'placeholder':'Est-ce le prochain match ou y en a-t-il un avant ? (si oui cocher)',
                                              'label':'Est-ce le prochain match ou y en a-t-il un avant ? (si oui cocher)',
                                              'class': 'form-check-input',
                                              })
        self.fields['isFinish'].widget.attrs.update({'id':'isFinish',
                                              'class': 'form-check-input',
                                              })
        self.fields['resultatEquipe1'].widget.attrs.update({'id':'resultatEquipe1',
                                              'placeholder':'Résultat Equipe 1',
                                              'class': 'form-control',
                                              })    
        self.fields['resultatEquipe2'].widget.attrs.update({'id':'resultatEquipe2',
                                              'placeholder':'Résultat Equipe 2',
                                              'class': 'form-control',
                                              })
        self.fields['resultatEquipe2'].required=False
        self.fields['resultatEquipe1'].required=False
        