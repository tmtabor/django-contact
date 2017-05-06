# django-contact

The intent of this project is to provide a simple contact form, where site users can leave feedback 
or otherwise send messages to the site admin or other associated individuals, without the need to 
publicly reveal an email address. The reCAPTCHA service is used to prevent spam.

## Requirements
* Python 2.7 or 3.5+
* Django 1.10+

## Setup Instructions
1. Copy the django-contact app into the appropriate directory.
2. Add the 'contact' to Django's INSTALLED_APPS list.
3. Configure the CONTACT_EMAIL, CONTACT_PREFIX and RECAPTCHA settings.
4. The app has no models, but you may still need to run Django's database migration.
