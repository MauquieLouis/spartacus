from django.urls import path

from . import views
    
app_name = 'main'         #permettra de différencier l'application utilisé lorsqu'on utilise {% url inside:detail %}
                            #dans le cas ou on aurais une autre application avec une vue nommé 'detail'
urlpatterns = [
    # / -> redirect to homepage
    path ('', views.home, name = 'home'),
    path ('organigramme/', views.organigramme1, name="orga1"),
    path ('organigrammev2/', views.organigrammeV2, name="orga2"),
    path ('organigrammev2/jakitunning/', views.organigrammeV2Effect, name="orga2Eff"),
    #path ('commande/wes', views.commande, name="commandeWES"),
    path ('commande/wes/<str:typem>/', views.commandeType, name="commandeWES"),
    path ('commande/wes/<str:typem>/correction/', views.commandeTypeCorrec, name="commandeWESCorrec"),
    path ('commande/wes/<str:typem>/horraire/', views.commandeTypeHorraire  , name="commandeWESHorraire"),
    path ('commande/wes/liste/personne/<str:type>/', views.listePersonnes ,name="listePersonne"),
    path ('commande/wes/gestion', views.gestionCommandes, name="commandeWESGestion"),
    path ('commande/wes/gestion/<int:command_id>/', views.gestionCommandesInfo, name="commandeWESGestionInfo"),
    path ('commande/wes/gestion/<int:command_id>/validornot/', views.validerOuNonCommande, name="validerCommande"),
    path ('commande/wes/gestion/<int:command_id>/delete', views.deleteCommande, name="deleteCommande"),
    path ('galerie/', views.galerie, name="galerie"),
    path ('link/verif/<str:link>/', views.verificationLink, name="verifLink"),
    path ('gestion/poles', views.gestionPoles, name="gestionPoles"),
    path ('gestion/poles/<int:id>/', views.gestionPoles, name="gestionPolesId"),
    path ('gestion/poles/<int:id>/delete/', views.deletePole, name="deletePole"),
    path ('poles/', views.motPoles, name="motPoles"),
    path ('gestion/galerie/', views.gestionGaleriePicture, name="gestionPictures"),
    path ('gestion/galerie/<int:id>/', views.gestionGaleriePicture, name="gestionPicturesId"),
    path ('gestion/galerie/<int:id>/delete/', views.deletePicture, name="deletePicture"),
    path ('shotgun/', views.shotgun, name="shotgun"),
    path ('scanCode/<str:link>/', views.scanCode, name="scanQrCode"),
#     path ('scanCode/<str:link>/', views.verifScanCode, name="scanQrCode"),
    path ('scanCode/<str:link>/verif/', views.verifScanCode, name="scanQrCodeVerif"),
    path ('scanCode/create/event/', views.createScanEvent, name="scanQrCodeCreateEvent"),
    path ('scanCode/show/list/', views.showScanEvent, name="scanQrCodeShowList"),
    
    path ('pronostic/liste/',views.listePronostic, name="listePronostic"),
    path ('pronostic/<int:pk>/detail/', views.detailPronostic, name="detailPronostic"),
    path ('pronostic/formulaire/',views.fairePronostic, name="fairePronostic"),
    path ('pronostic/match/create/',views.createMatch, name="createMatch"),
    path ('pronostic/match/<int:pk>/edit/',views.modifyMatch, name="editMatch"),
    path ('pronostic/match/gestion/', views.gestionMatch, name="gestionMatch"),
    path ('pronostic/match/<int:pk>/delete', views.deleteMatch, name="deleteMatch"),
    
    path ('presentation',views.pdfView,name="pdfView"),
    
    path('campagne/commande/', views.commandeCampagneType, name="commandeCampagneType"),
    path('campagne/liste/commande/', views.listeCampagneCommande, name="listeCampagneCommande"),
    path('campagne/liste/commande/nonValid/', views.listNonValid, name="listNonValid"),
    path('campagne/commande/<int:pk>/',views.changementCommande, name="changementCommande"),
    path('campagne/commande/<int:pk>/delete',views.deleteCampagneCommande, name="deleteCampagneCommande"),
    
    # /inside/5/
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    ]
