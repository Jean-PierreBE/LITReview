# Projet 9 OpenClassRoom : écrire un site web avec DJANGO
## Présentation du projet
Le but de ce projet est de créer un site web avec le framework django. Ce site web permet à un ensemble d'utilisateurs de demander des critiques
, de créer des critiques sur des ouvrages et de les partager. Pour cela un utilisateur a le choix de choisir avec qui il veut partager ses demandes 
et ses critiques. Il pourra choisir n'importe quel utilisateur et le révoquer également à tout moment.

## composition
Tous les fichiers .py, html css necessaires au fonctionnement du logiciel se trouvent dans le répertoire src.
Les autres fichiers sont :
- README.md qui contient des informations sur le logiciel
- requirements.txt contient les packages necessaires au bon fonctionnement du logiciel
- tox.ini permet de paramétrer flake8 pour voir si le programme répond aux normes pep8

## Installation de l'application
- Cloner le dépôt de code à l'aide de la commande `https://github.com/Jean-PierreBE/LITReview.git`
- Rendez-vous depuis un terminal à la racine du répertoire LITReview avec la commande `cd LITReview`
- Créer un environnement virtuel pour le projet avec `$ python -m venv env` sous windows ou `$ python3 -m venv env` sous macos ou linux.
- Activez l'environnement virtuel avec `$ env\Scripts\activate` sous windows ou `$ source env/bin/activate` sous macos ou linux.
- installer les packages python du fichier requirements.txt en lançant la commande suivante 
  - `pip install -r requirements.txt`

les packages installés sont les suivants :
- django : framework permettant de développer les sites webs

## Lancement du programme
On lance le programme en tapant sur la ligne de commande dans le répertoire src:
- `python manage.py runserver`

## Déroulement du programme
Une fois la commande précédente exécutée, mettre l'adresse suivante
- `http://127.0.0.1:8000/`
dans le browser de votre choix.
- Un écran demandant de vous connecter apparaît. Pour cela rentrez un pseudo et mot de passe.
Si vous n'en avez pas , vous pouvez vous inscrire en cliquant sur le bouton s'inscrire.
Pour vous inscrire , vous avez besoin d'un pseudo (unique) , d'une adresse mail (unique) et de saisir deux fois
le mot de passe. Une fois ces informations validées vous revenez sur l'écran d'accueil.
- Une fois connecté , vous arrivez sur l'écran principal. Sur cet écran , vous avez la possibilité de voir toutes les critiques et tickets 
émis par vous ainsi que ceux de vos correspondants. Vous avez également le choix de créer une critique et de créer un ticket (demande de critique).
Ces critiques et tickets se retrouveront dans l'écran posts(bouton posts). Pour choisir vos correspondants , vous pouvez aller sur l'écran Abonnements
bouton abonnements. Le bouton flux permet de revenir sur l'écran principal. Et évidemment il y a le bouton déconnecter qui permet de quitter l'application.
- l'écran demander une critique permet de créer un ticket , il est possible de télécharger une image.
- l'écran créer une critique permet de créer une critique sans ticket demandé par un autre utilisateur. Un ticket affecté à l'utilisateur sera créé d'office.
- l'écran abonnements permet d'ajouter et ou de supprimer d'autres utilisateurs. Pour ajouter un utilisateur , il suffit de rentrer un code pseudo puis de valider.
La liste des utilisateurs suivis s'affichent en dessous. Un bouton supprimer permet se supprimer un utilisateur. L'utilisateur a la possibilité également de voir
si il est suivi ou non.
- l'écran posts permet de voir les critiques et tickets qu'il a émis. Il peut modifier ou supprimer uniquement ses propres tickets et critiques. Si il a écrit une
critique en réponse à un ticket , seule la critique sera supprimée. Si il veut supprimer un ticket et qu'une critique a été émise par un autre utilisateur , 
la critique et le ticket seront supprimés.
- l'écran flux reprend les critiques et tickets de l'utilisateur connecté ainsi que ceux des utilisateurs qu'il suit. L'utilisateur peut créer des critiques en
réponses à des tickets que si ces tickets n'ont pas de critiques.


## Contrôle qualité
Pour vérifier la qualité du code , on peut lancer la commande suivante :
- `flake8 --format=html --htmldir=flake-report src`
Le rapport sortira en format html dans le répertoire flake-report

pour cela il faut installer :
- flake8 : contrôle du code pour vérifier la compatibilité avec les normes pep8
- flake8-html : permet de sortir le rapport flake8 sous format html
- flake8-functions : permet d'ajouter des contrôles au niveau des fonctions (ex : longueur maximale des fonctions)

le fichier tox.ini contient la configuration pour flake8.
- `max-line-length = 120` : la longueur maximale de chaque ligne ne peut pas dépasser 119 caractères
- `max-function-length = 50` : la longueur maximale de chaque fonction ne peut pas dépasser 50 lignes
- `ignore = CFQ002, CFQ004, W503, W504` : évite les erreurs
  - CFQ002 : nombre d'arguments en entrée trop élevés (> 6)
  - CFQ004 : nombre d'éléments en retour trop élevés (> 3)
  - W503 : saut de ligne avant un opérateur
  - W504 : saut de ligne après un opérateur

Ces paramètres peuvent être modifiés
