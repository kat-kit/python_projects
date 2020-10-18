# Données de comptes individuels des regions

Scripts d'extraction et de remise en forme des données des comptes individuels des regions selon plusieurs criteres( années, regions, format, ..).

## Prerequis pour lancer le projet

Le lancement du projet necessite etre sur un envirennement linux et python 3
sur windows on peu utiliser ubuntu pour windows le lien suivant montre les etapes à suivre pour installer l'application à partir du windows store et le parametrage pour faire fonctionner l'environnement:
https://www.youtube.com/watch?v=vL3Yy4rtLjE&ab_channel=Telusko

ensuite on part sur l'emplacement C:\Users\non_utilisateur\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\home\nom_utilisateur_ubuntu
et on colle le projet

nom_utilisateur: est le non utilisateur dans le PC
nom_ubuntu est le nom qu'on montionne lorsque on accède pour la 1ere fois à l'appli ubuntu

on lance la commande: cd nom_projet_telechargé
et en suite on lance la commande:
pip install -r requirements.txt
pour installer les dependance necessaire pour la partie python

Il se peux que pip n'est pas installé dans ce cas on peu lancer les deux commandes:
sudo apt update : pour rafraichir les packages du systeme
sudo apt install python3-pip : pour installet pip pour python 3

## Structure et Lancement du projet:

Le projet est composé des fichiers suivants:

# download_region.py

Ce script python appels le web service des telechargements exposé par le ministère sur le lien https://data.economie.gouv.fr/explore/dataset/comptes-individuels-des-regions-fichier-global/export/

il envoi une requête http permettant de telecharger automatiquement le fichier contenant les statistique des regions selon les criteres passé en parametre

## 3 shells linux:

# batch_regions_data_by_region.sh

Ce batch permet de lancer le ficher download_region.py pour chaque region stockée dans le array regions et telecharger les fichers xls et les mettre dans le dossiers regions_data xlsfile/region

# batch_regions_data_by_year_region.sh

1-Ce batch permet de creer une archetecture de dossier annee/regions
ensuite lancer le fichier download_region.py pour telecharger les données specifique à chaque année et region et le mettre dans l'emplacement approprié. (exemple (année =2008, region=011 le fichier sera positionné dans 2008/011/nom_du_fichier.csv))
2- Ce shell permet egalement de lancer le download pour telecharger toutes les données des régions sans mettre des critères

# batch_regions_data_by_year.sh

Ce shell permet de creer un archetecture en dossiers portant les nom des années et de telecharger les données specifiques pour chaque année et de positionnée dans le dossier de chaque année le fichier spacifique contenant les statistique de cette année.

Note: dans les shell batch_regions_data_by_year_region.sh on peut bien changer les années de DEBUT et de FIN
on pout aussi commenter la 1ere partie et lancer que les derniere partie pour telecharger le fichier global

Merci de ne pas prendre en consideration les fautes d'orthographe sur ce document hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh
