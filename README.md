# Application de Gestion de Pharmacie

## Description

Cette application est conçue pour faciliter la gestion des pharmacies. Développée en Django et utilisant PostgreSQL comme base de données, elle offre une interface intuitive pour gérer les médicaments, les ventes, et les stocks.

## Fonctionnalités

- **Gestion des Médicaments**
  - Ajout, modification et suppression de médicaments.
  - Consultation des informations détaillées sur chaque médicament (nom, dosage, prix, etc.).
  
- **Gestion des Stocks**
  - Suivi des niveaux de stock pour chaque médicament.
  - Alertes pour les médicaments à faible stock.

- **Gestion des Ventes**
  - Enregistrement des ventes de médicaments.
  - Génération de reçus pour les clients.
  - **Gestion des Fournisseurs**
  - Ajout et gestion des informations des fournisseurs de médicaments.
  - Historique des transactions avec chaque fournisseur.

- **Rapports**
  - Génération de rapports sur les ventes, les stocks, et les médicaments les plus vendus.
  - Statistiques de performance mensuelles et annuelles.

- **Interface Utilisateur**
  - Interface web conviviale et responsive.
  - Authentification des utilisateurs avec différents niveaux d'accès (administrateur, pharmacien).

## Prérequis

- Python 3.x
- Django
- PostgreSQL
- Pip

## Installation
1. Clonez le dépôt :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo


   python -m venv env
source env/bin/activate  # Sur Windows, utilisez `env\Scripts\activate`

Installez les dépendances :
pip install -r requirements.txt

Appliquez les migrations :
python manage.py migrate

Lancez le serveur de développement :
python manage.py runserver
