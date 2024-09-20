Models
===============

The OC Lettings project database uses SQLite and is structured with the following models, divided into two apps: `profiles` and `lettings`.

Models in the `profiles` app
----------------------------

- **User**: Django's default user model.
- **Profile**: A model for user profiles with the following fields:

  - `user`: The associated user (OneToOneField).
  - `favorite_city`: The user's favorite city (CharField).

Models in the `lettings` app
----------------------------

- **Address**: A model for an address with the following fields:

  - `number`: House number (PositiveIntegerField).
  - `street`: Street name (CharField).
  - `city`: City name (CharField).
  - `state`: State code (CharField, 2 characters).
  - `zip_code`: Postal code (PositiveIntegerField).
  - `country_iso_code`: Country ISO code (CharField, 3 characters).

- **Letting**: A model for a rental property with the following fields:

  - `title`: Rental title (CharField).
  - `address`: The associated address (OneToOneField).

Generated tables by these models
-------------------------------

- **auth_user**: Default table for users.
- **profiles_profile**: Table for user profiles.
- **lettings_address**: Table for addresses.
- **lettings_letting**: Table for rental properties.

These tables store and manage user and rental property information within the OC Lettings application.
