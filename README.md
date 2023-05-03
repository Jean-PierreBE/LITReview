# Projet 9 OpenClassRoom : écrire un site web avec DJANGO
## Présentation du projet
Le but de ce projet est de créer un logiciel de gestion de tournois d'échecs qui fonctionne hors ligne.
8 joueurs participent à un tournoi qui se compose de 4 rounds et chaque round comprend 4 matchs avec 2 joueurs chacun,suivant l'algorithme suisse (voir description plus bas).
Avec le logiciel développé , les organisateurs vont pouvoir créer les joueurs (8 au minimum) , encoder les tournois et
sortir des rapports sur le déroulement des tournois.
Chaque tournoi pourra être arrêté temporairement à tout moment durant son déroulement pour diverses raisons : heure tardive, 
joueur malade , élément imprévu.
Le score de chaque match pourra être modifié durant chaque round.

## composition
Tous les fichiers .py necessaires au fonctionnement du logiciel se trouvent dans le répertoire ProjectTournoi.
Les autres fichiers sont :
- README.md qui contient des informations sur le logiciel
- requirements.txt contient les packages necessaires au bon fonctionnement du logiciel
- tox.ini permet de paramétrer flake8 pour voir si le programme répond aux normes pep8

## Installation
- choisissez votre répertoire où exécuter vos programmes python
- créer votre environnement virtuel
- installer les packages python du fichier requirements.txt en lançant la commande suivante 
  - `pip install -r requirements.txt`

les packages installés sont les suivants :
- tinydb : gestion de la base de données tinydb
- prettytable : gestion de tableau pour les différents affichages
- jsons : permet de sérializer les objets pour les intégrer dans tinydb

## Lancement du programme
On lance le programme en tapant sur la ligne de commande :
- `python -m ProjectTournoi`

## Déroulement du programme
On lance la commande ci-dessus et un menu avec 9 options apparaît
Seul un chiffre entre 1 et 9 peut être encodé , sinon un message d'erreur apparaît.
- option 1 : permet de créer des joueurs , les champs demandés sont nom, prénom, genre, date de naissance et classement.Le classement débute à 1000(enfant) et se termine à 2800(joueur de classe internationale) suivant le classement ELO.Les champs obligatoires sont nom, prénom, genre et classement. Des contrôles sont éffectués , le code genre ne peut comprendre que M (masculin) ou F (féminin).Le classement doit être numérique et compris entre 1000 et 2800.Une fois le joueur encodé, le programme propose de continuer. Si l'utilisateur choisit de quitter, tous les joueurs encodés sont stockés dans une base tinydb.
- option 2 : permet de modifier les joueurs déja créés. Si aucun joueur n'a été encodé, un message d'erreur apparait. Si des joueurs ont été encodés, une liste des joueurs apparaît. Il suffit de sélectionner l'indice et de modifier les différents champs.Si l'utilisateur n'encode rien, la valeur initiale est conservée. Les contrôles sur le code genre,date de naissance, classement sont les mêmes qu'en cas de création si il y a une modification.
- option 3 : permet la création d'un tournoi. Le programme demande d'encoder le lieu , date ,description. L'encodage du lieu, description est obligatoire. Si on ne renseigne pas la date, la date du jour est automatiquement sélectionnée. En cas de saisie de date , un contrôle est quand même éffectué. Une liste de joueurs apparaît (8 au minimum) , si il n'y a pas 8 joueurs le programe signale le nombre de joueurs manquants à encoder. L'organisateur sélectionne les joueurs , le programme contrôle qu'un joueur ne soit pas sélectionné 2 fois. Une fois les joueurs encodés, on commence à encoder le 1er round avec la date et l'heure. Si on n'encode rien, la date du jour et l'heure actuelle sont encodées. Une fois le round crée , la liste des matchs avec les joueurs apparaît suivant l'algorithme suisse. Le programme demande si le round est terminé , si on tape 'N' , on demande le numéro de match pour encoder le score , on peut saisir de 1 à 4. Une fois le match on encode le score , `0 : match nul` , `1 : joueur A vainqueur` , `2 : joueur B vainqueur`. On peut modifier le résultat du match autant de fois qu'on veut tant que le round n'est pas terminé. Dès que tous les matchs sont encodés on indique que le round est terminé. On pense au round suivant jusqu'au dernier round. Entre chaque round , il est possible de continuer ou non le tournoi. Que l'on aille jusqu'au bout ou non le résultat du tournoi est stocké en base de données.
- option 4 : permet de modifier , de terminer ou de recommencer un tournoi. Le programme affiche la liste de tous les tournois. On sélectionne un tournoi et on peut choisir un round. Mais si le tournoi choisi n'a que 2 rounds , on peut sélectionner jusquà 3 rounds ou recommencer au premier. Si on sélectionne un round déja joué, les résultats de ce round sont éffacés. Une fois le round sélectionné, le déroulement du tournoi se déroule comme dans l'option 3. On peut modifier autant de tournois que l'on veut.
- option 5 : Affiche la liste des joueurs par ordre alphabétique
- option 6 : Affiche la liste des joueurs par classement (ordre croissant)
- option 7 : Affiche la liste des tournois , lieux ,date , description
- option 8 : La liste de tous les tournois encodés s'affiche , on sélectionne un tournoi et les tableaux suivants apparaissent
  - lieu ,date ,description  
  -  liste des joueurs
  -  liste des rounds avec date de début, heure de début, date de fin, heure de fin
  -  liste des résultats par rounds et matchs
  -  Résultats du tournoi par joueurs     
- option 9 : quitte le programme

## Contrôle qualité
Pour vérifier la qualité du code , on peut lancer la commande suivante :
- `flake8 --format=html --htmldir=flake-report ProjectTournoi`
Le rapport sortira en format html dans le répertoire flake-report

pour cela il faut installer :
- flake8 : contrôle du code pour vérifier la compatibilité avec les normes pep8
- flake8-html : permet de sortir le rapport flake8 sous format html
- flake8-functions : permet d'ajouter des contrôles au niveau des fonctions (ex : longueur maximale des fonctions)

le fichier tox.ini contient la configuration pour flake8.
- `max-line-length = 119` : la longueur maximale de chaque ligne ne peut pas dépasser 119 caractères
- `max-function-length = 50` : la longueur maximale de chaque fonction ne peut pas dépasser 50 lignes
- `ignore = CFQ002, CFQ004` : évite les erreurs
  - CFQ002 : nombre d'arguments en entrée trop élevés (> 6)
  - CFQ004 : nombre d'éléments en retour trop élevés (> 3)

Ces paramètres peuvent être modifiés
