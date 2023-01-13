## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/Prud-homme/Python-OC-Lettings.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(profiles_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  profiles_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Déploiement

Mon application Heroku est disponible à l'adresse `http://oc-lettings-56.herokuapp.com/`

#### Prérequis

- Disposer d'un compte sur les SaaS suivants: Circle CI, Docker, Heroku.
- Avoir relier le compte Github contenant le repository de l'application à celui de CircleCI.
- Configurer les variables d'environnements CircleCI du projet de l'application:
  - `DOCKERHUB_USERNAME`: identifiant du compte DockerHub
  - `DOCKERHUB_PASSWORD`: mot de passe du compte DockerHub
  - `HEROKU_APP_NAME`: nom de l'application sur Heroku (oc-lettings-56 pour ce repository)
  - `HEROKU_API_KEY`: clé API de l'application sur Heroku

#### Récapitulatif
Chaque push sur le repository GitHub déclenche un workflow de Circle CI:

- (workflow *prod*) Si la modification concerne la branche main alors les jobs suivants seront exécutés dans cet ordre et seulement si le précédent job s'est effectué avec succès:
  - `build-and-test`: les packages du fichier requirements.txt sont installé puis la suite de tests est exécuté
  - `push-to-dockerhub`: à l'aide du DockerFile, une image Docker de l'application est créé et stockée dans le repository DockerHub. Chaque image Docker est taguée avec le "hash" de commit CirclecI. 
  - `deploy-to-heroku`: l'image Docker de l'application est déployé sur Heroku

- (workflow *dev*) Si la modification ne concerne pas la branche main, seul le job `build-flake8-test` est exécuté: les packages du fichier requirements.txt sont installé, exécution du linting puis de la suite de tests/

Les workflows et jobs sont configuré dans le fichier `config.yml` du dossier `.circleci`.

#### Création et lancement en local d'une image de l'application

Il faut commencer par se placer à la racine du repertoire contenant le projet puis lancer la commande suivante : `docker build -t <IMAGE_NAME> . && docker run -d -p 8000:8000 <IMAGE_NAME>`

*`IMAGE_NAME` correspond au nom que vous souhaitez donner à l'image de l'application.*

Il suffit ensuite d'aller à l'adresse `http://localhost:8000` pour accèder à l'application.

#### Déploiement d'une image de l'application sur Heroku

Les commandes suivantes seront lancées en se placant à la racine du repertoire contenant le projet.

Création et push d'une nouvelle image sur Docker:

- Connexion à Docker: `docker login --username <DOCKERHUB_USERNAME> --password <DOCKERHUB_PASSWORD>`
- Création de l'image: `docker build -t <DOCKERHUB_USERNAME>/<REPOSITORY>:<TAG> .`
- Push de l'image sur Docker: `docker push <DOCKERHUB_USERNAME>/<REPOSITORY>:<TAG>`

Déploiement d'une image existante sur Docker:

- Connexion a Heroku: `heroku container:login`
- Push d'une image existante sur Heroku: `docker tag <IMAGE_ID> registry.heroku.com/<HEROKU_APP_NAME>/web` puis `docker push registry.heroku.com/<HEROKU_APP_NAME>/web`
- Déploiement de l'image: `heroku container:release -a <HEROKU_APP_NAME> web`

Il suffit ensuite d'aller à l'adresse `http://<HEROKU_APP_NAME>.herokuapp.com/` pour accèder à l'application.

*`<REPOSITORY>` correspond au répertoire dans lequel seront stocké les images.*

*`TAG` correspond au tag de l'image qui a été générée.*

*`<IMAGE_ID>` correspond à l'id de limage docker que l'on souhaite poussée.*

### Sentry

...
