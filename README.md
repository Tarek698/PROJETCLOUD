# Mon Blog Personnel

Bienvenue sur **Mon Blog Personnel**, une application web simple développée avec Flask et intégrée à Azure pour la gestion des commentaires et l'analyse de sentiment via le service Text Analytics. Ce projet est conçu pour offrir une expérience utilisateur esthétique et fonctionnelle.

## Table des matières
- [Aperçu du projet](#aperçu-du-projet)
- [Fonctionnalités](#fonctionnalités)
- [Architecture](#architecture)
- [Technologies utilisées](#technologies-utilisées)
- [Prérequis](#prérequis)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Déploiement sur Azure](#déploiement-sur-azure)
- [Prochaines améliorations](#prochaines-améliorations)

---

## Aperçu du projet
Ce projet est un blog personnel où les utilisateurs peuvent :
1. Voir une liste d'articles.
2. Consulter un article en particulier.
3. Ajouter des commentaires sur chaque article.
4. Voir une analyse de sentiment sur chaque commentaire.

Les commentaires sont stockés dans un **Azure Blob Storage**, et l'analyse de sentiment est réalisée à l'aide du service **Azure Text Analytics**.

---

## Fonctionnalités
- **Page d'accueil** : Liste des articles disponibles.
- **Détails d'un article** : Contenu de l'article avec une section dédiée aux commentaires.
- **Commentaires** : Ajout de commentaires avec une analyse de sentiment automatique (positif, neutre, négatif).
- **Intégration Azure** :
  - Stockage des commentaires dans un conteneur Blob Storage.
  - Analyse de sentiment via Azure Cognitive Services (Text Analytics).
  - Azure WebApp
  
---

## Architecture
Le projet est structuré comme suit :
├── app.py # Fichier principal Flask ├── templates # Fichiers HTML pour le rendu │ ├── base.html # Template de base │ ├── index.html # Page d'accueil │ ├── article.html # Page de détail d'un article ├── static │ ├── style.css # Feuille de style CSS ├── blob_utils.py # Gestion des interactions avec Azure Blob Storage ├── README.md # Documentation du projet └── requirements.txt # Dépendances Python

---

## Technologies utilisées
- **Frontend** :
  - HTML
  - CSS (esthétique améliorée avec des éléments comme une barre de navigation et des cartes d'articles)
- **Backend** :
  - Python 3.12
  - Flask
- **Azure** :
  - Azure Blob Storage
  - Azure Text Analytics

---

## Prérequis
1. **Python** (version 3.12 recommandée)
2. Un compte Azure avec les services suivants configurés :
   - Azure Storage Account avec un conteneur nommé `blogfiles`.
   - Azure Text Analytics avec une clé API.
3. **Git** pour la gestion du code source.

---

## Installation
1. Clonez le dépôt :
   ```bash
   git clone <URL_DU_DEPOT>
   cd <NOM_DU_PROJET>

2. Installez les dépendances Python :
pip install -r requirements.txt

3. Configurez les variables d'environnement Azure :
$env:AZURE_STORAGE_ACCOUNT="votre_nom_de_compte_storage"
$env:AZURE_STORAGE_KEY="votre_clé_de_stockage"
$env:TEXT_ANALYTICS_ENDPOINT="votre_endpoint_text_analytics"
$env:TEXT_ANALYTICS_KEY="votre_clé_text_analytics"

4. Lancez l'application :
python app.py

5. Accédez à l'application dans votre navigateur :
http://127.0.0.1:5000

## Utilisation

Accédez à la page d'accueil pour voir la liste des articles.
Cliquez sur un article pour voir son contenu.
Ajoutez un commentaire et observez l'analyse de sentiment qui s'affiche (positif, neutre ou négatif).
Retournez à l'accueil en cliquant sur le bouton dédié.

## Déploiement sur Azure

Créer les ressources Azure :
Suivez ces commandes pour configurer les services nécessaires : 

az storage account create --name <nom_du_compte> --resource-group <groupe_ressource> --location <région>
az storage container create --account-name <nom_du_compte> --name blogfiles
az cognitiveservices account create --name <nom_service_text_analytics> --resource-group <groupe_ressource> --kind TextAnalytics --sku S --location <région>

Déployer le code :

Configurez un dépôt Git Azure ou GitHub et poussez le code.
Configurez un service App Service pour exécuter l'application Flask.
Vérifier le déploiement :

Accédez à l'URL de votre service Azure pour tester l'application.

Notes importantes
Test des commentaires : Les commentaires soumis sont stockés dans Azure Blob Storage. Pensez à vider ou vérifier régulièrement les données si elles contiennent des tests.
Analyse de sentiment : Vérifiez que votre clé Azure Text Analytics est valide.

Auteur
Projet réalisé par Bessad Tarek dans le cadre d'un exercice académique pour démontrer l'intégration de Flask avec Azure.
