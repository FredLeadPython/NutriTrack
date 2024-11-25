# NutriTrack - Clean Architecture Overview

NutriTrack utilise la **Clean Architecture**, une approche modulaire et maintenable qui sépare clairement les responsabilités des différentes couches de l'application. Cette architecture garantit une flexibilité, une testabilité et une évolutivité optimales.

---

## Clean Architecture - Aperçu

La Clean Architecture est basée sur des principes de séparation des préoccupations et de dépendance inverse. Elle structure le projet en plusieurs couches indépendantes :

### Schéma simplifié :

1. **Domain** : Le cœur métier de l'application (entités et règles métier).
2. **Application** : Les cas d'utilisation ou la logique applicative.
3. **Interface** : La couche de présentation et d'interaction utilisateur (exemple : API FastAPI).
4. **Infrastructure** : La gestion des technologies externes comme la base de données.

---

## Description des couches

### 1. **Domain**

Le **cœur de l'application**, indépendant de toute technologie externe.

Il contient :
- **Entités** : Représentation des objets métier (ex. : `User`, `Meal`, etc.).
- **Interfaces** : Contrats définissant comment les données seront manipulées (repositories).

### 2. **Application**
Contient les cas d'utilisation (ou services). Cette couche orchestre les interactions entre les entités du domaine et les technologies externes.

### 3. **Interface**
La couche responsable de l'interaction utilisateur. Dans ce projet, il s'agit de l'API REST basée sur FastAPI.

Routes définies dans interface/api/endpoints/.
Les endpoints utilisent les cas d'utilisation pour exécuter la logique.

### 4. **Infrastructure**
La couche où sont implémentées les dépendances externes :

Connexion à la base de données.

Implémentation concrète des interfaces définies dans Domain.


## Avantages de la Clean Architecture

1. **Séparation claire des responsabilités** : Chaque couche a une fonction bien définie, ce qui facilite la compréhension et la maintenance.

2. **Indépendance des technologies** : Le domaine métier est indépendant des outils (frameworks, bases de données).

3. **Facilité de test** : Les tests unitaires peuvent être écrits pour chaque couche indépendamment.

4. **Évolutivité** : Vous pouvez facilement remplacer une implémentation ou ajouter une nouvelle fonctionnalité sans affecter le reste de l'application.
