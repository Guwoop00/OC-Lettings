API
==========

Le projet OC Lettings propose plusieurs interfaces pour gérer les profils et les locations.

Interface d'Administration Django
---------------------------------

L'interface d'administration Django permet aux administrateurs de gérer les données de l'application. Les fonctionnalités incluent l'ajout, la consultation, la modification et la suppression des profils et des locations.

- URL : /admin/
- Fonctionnalités : CRUD (Create, Read, Update, Delete) pour les modèles Profile, Letting, et Address.

Interface Graphique du Site
---------------------------

L'interface graphique permet aux utilisateurs de visualiser les profils et les locations à travers différentes pages.

- **Page d'accueil** :
    - URL : /
    - Vue : `index` - Affiche la page d'accueil avec un message de bienvenue.

- **Page des Locations** :
    - URL : /lettings/
    - Vue : `lettings_index` - Affiche la liste des locations disponibles.
    - URL : /lettings/<letting_id>/
    - Vue : `letting_detail` - Affiche les détails d'une location spécifique.

- **Page des Profils** :
    - URL : /profiles/
    - Vue : `profiles_index` - Affiche la liste des profils d'utilisateurs.
    - URL : /profiles/<username>/
    - Vue : `profile_detail` - Affiche les détails d'un profil utilisateur spécifique.
