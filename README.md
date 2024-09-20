# OC Lettings

OC Lettings is a property rental management platform developed with Django. This project includes features to manage rentals, addresses, and user profiles.

## Project Description

OC Lettings allows users to easily manage rental listings, view property details, and manage user information via an admin interface. The application has been developed following best practices with complete test coverage, continuous integration (CI/CD), and is containerized with Docker for easy deployment.

## Installation

To install the OC Lettings project, you will need:

- Python 3.11 or higher
- A GitHub account with defined secrets
- An AWS or Render account configured for deployment
- A DockerHub account

### Installation Steps:

1. Clone the repository from GitHub:

   ```bash
   git clone https://github.com/Guwoop00/OC-Lettings.git

2. Navigate to the project directory:

    ```bash
    cd OC-Lettings

3. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # (On   Windows: venv\Scripts\activate)

4. Install the dependencies:

    ```bash
    pip install -r requirements.txt

## Quick Start Guide

To quickly start with OC Lettings, follow these steps:

1. Apply database migrations:

    ```bash
    python manage.py migrate

2. Create a superuser to access the admin interface:

    ```bash
    python manage.py createsuperuser

3. Run the Django development server:

    ```bash
    python manage.py runserver

4. Open your browser and go to:

    ```bash
    http://localhost:8000

5. Access the admin interface at:

    ```bash
    http://127.0.0.1:8000/admin/

Use the credentials you set up with the createsuperuser command.


## Technologies and Programming Languages

Python: Core language used for the backend with Django.
Django: Web framework used for building the platform.
Docker: Containerization for easier deployment.
GitHub Actions: CI/CD pipeline to automate tests, build, and deployment.

## Database Structure and Data Models

The OC Lettings project uses Django's ORM for database management. Here is an overview of the key models:

Address: Stores details of the rental property’s location.
Letting: Represents a rental listing with related information.
Profile: Represents user data, linked to the Django User model.

## API Description

OC Lettings exposes some RESTful APIs for managing rentals, addresses, and profiles. API documentation is included for integrating with these endpoints. API calls allow you to:

List and retrieve rental properties.
Add, update, or delete rental listings.
Manage user profiles.

## Usage Guide

Use Case 1: Managing Rental Listings

Go to the admin panel to manage rental properties.
Add a new property by filling in the required fields such as address, rental price, and property description.
Save the changes and view the updated listings.
Use Case 2: User Profile Management

In the admin panel, navigate to the Profiles section.
Update user information such as their contact details and preferences.
Save and verify the changes.

## Deployment and Application Management Procedures

The project is deployed using Render and Docker containers. Follow these steps to deploy:

### CI/CD Pipeline and Deployment

The CI/CD pipeline is set up using GitHub Actions and Docker. Here’s an overview:

Testing and Linting: The code is linted with flake8 and tested using Django’s testing framework with a coverage threshold of 80%.
Containerization: The application is containerized using Docker and pushed to DockerHub. Each Docker image is tagged with the commit hash.
Deployment: The application is deployed to Render. Only changes to the main branch trigger the containerization and deployment processes.

### Deployment Instructions for Render:

Render automatically detects any changes in the GitHub repository, builds the Docker container, and deploys it to production.
Ensure that static files are correctly loaded post-deployment and that the admin interface is functional.
Use environment variables in Render for secrets and configuration.

### Post-Deployment Management:

Ensure that the application runs smoothly and monitor for any errors using the logs from Render.
Manage scaling and performance settings directly from the Render dashboard.

## Additional Documentation

The project documentation is built with Sphinx and hosted on Read the Docs. The following sections are included:

-Project Description: Overview of the OC Lettings platform.
-Installation Instructions: How to set up the project locally.
-Quick Start Guide: Steps to get the development server running.
-Database Models: Detailed descriptions of data models.
-API Guide: Documentation for the API endpoints.
-Deployment Procedures: Instructions for deploying the project to Render or other hosting services.