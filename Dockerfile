# Base image
FROM python:3.9-slim

# Install dépendancies
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy code source
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Exposer le port du serveur
EXPOSE 8000

# Lancer le serveur Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]