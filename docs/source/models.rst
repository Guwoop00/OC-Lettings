Models
===============

La base de données du projet OC Lettings utilise SQLite et est structurée avec les modèles suivants, répartis dans deux applications : `profiles` et `lettings`.

Modèles de l'application `profiles`
-----------------------------------

- **User** : Modèle par défaut de Django pour les utilisateurs.
- **Profile** : Modèle pour les profils des utilisateurs avec les champs suivants :

  - `user` : L'utilisateur associé (OneToOneField).
  - `favorite_city` : La ville favorite de l'utilisateur (CharField).

Modèles de l'application `lettings`
-----------------------------------

- **Address** : Modèle pour une adresse avec les champs suivants :

  - `number` : Numéro de la maison (PositiveIntegerField).
  - `street` : Nom de la rue (CharField).
  - `city` : Nom de la ville (CharField).
  - `state` : Code de l'état (CharField, 2 caractères).
  - `zip_code` : Code postal (PositiveIntegerField).
  - `country_iso_code` : Code ISO du pays (CharField, 3 caractères).

- **Letting** : Modèle pour une location avec les champs suivants :

  - `title` : Titre de la location (CharField).
  - `address` : Adresse associée (OneToOneField).

Tables générées par ces modèles
-------------------------------

- **auth_user** : Table par défaut pour les utilisateurs.
- **profiles_profile** : Table pour les profils des utilisateurs.
- **lettings_address** : Table pour les adresses.
- **lettings_letting** : Table pour les locations.

Ces tables permettent de stocker et gérer les informations des utilisateurs et des locations dans OC Lettings.
