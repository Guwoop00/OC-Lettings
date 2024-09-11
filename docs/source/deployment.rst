Deployment
==========

Pour déployer le projet OC Lettings sur Render, suivez les étapes ci-dessous.

Pré-requis
----------
- Un compte Render.
- Un dépôt GitHub avec le projet OC Lettings.

Étapes de Déploiement
---------------------

**1. Connectez Render à GitHub :**

   - Connectez-vous à votre compte Render.
   - Accédez à la page des intégrations et autorisez Render à accéder à votre compte GitHub.

**2. Créez un nouveau service Web sur Render :**

   - Cliquez sur "New Web Service" sur le tableau de bord de Render.
   - Connectez votre dépôt GitHub contenant le projet OC Lettings.
   - Sélectionnez la branche que vous souhaitez déployer (par exemple, `main`).

**3. Configurez les paramètres du service :**

   - **Build Command** : `docker build -t guwoop/oc_lettings_site:$RENDER_GIT_COMMIT .`
   - **Start Command** : `docker run -p 80:8000 guwoop/oc_lettings_site:$RENDER_GIT_COMMIT`
   - **Environment Variables** : Ajoutez les variables d'environnement nécessaires (voir section `.env`).

**4. Déployez le service :**

   - Cliquez sur "Create Web Service" pour démarrer le déploiement.
   - Render construira et déploiera automatiquement votre application.

**5. Vérifiez le déploiement :**

   - Une fois le déploiement terminé, Render vous fournira une URL pour accéder à votre application.
   - Assurez-vous que tout fonctionne correctement en visitant l'URL fournie.

Notes
------
- Vous pouvez configurer des déploiements automatiques pour chaque push vers la branche sélectionnée en activant l'option correspondante sur Render.
- Vérifiez les logs de déploiement sur Render en cas de problème pour diagnostiquer les erreurs.
