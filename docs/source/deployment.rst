### Deployment
==========

To deploy the OC Lettings project on Render, follow the steps below.

#### Prerequisites
----------
- A Render account.
- A GitHub repository containing the OC Lettings project.

#### Deployment Steps
---------------------

**1. Connect Render to GitHub:**

   - Log in to your Render account.
   - Go to the integrations page and authorize Render to access your GitHub account.

**2. Create a new Web Service on Render:**

   - Click on "New Web Service" from the Render dashboard.
   - Connect your GitHub repository containing the OC Lettings project.
   - Select the branch you want to deploy (e.g., `main`).

**3. Configure the service settings:**

   - **Build Command**: `docker build -t guwoop/oc_lettings_site:$RENDER_GIT_COMMIT .`
   - **Start Command**: `docker run -p 80:8000 guwoop/oc_lettings_site:$RENDER_GIT_COMMIT`
   - **Environment Variables**: Add the necessary environment variables (refer to the `.env` section).

**4. Deploy the service:**

   - Click on "Create Web Service" to initiate the deployment.
   - Render will automatically build and deploy your application.

**5. Verify the deployment:**

   - Once the deployment is complete, Render will provide you with a URL to access your application.
   - Ensure everything works properly by visiting the provided URL.

#### Notes
------
- You can enable automatic deployments for each push to the selected branch by activating the appropriate option on Render.
- Check the deployment logs on Render if any issues arise to troubleshoot errors.
