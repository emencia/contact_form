emencia-contact-form-maintenance
================================

**Package has moved from 'emencia-contact-form' to 'emencia-contact-form-maintenance' due to an ownership problems on Pypi, all release up to 0.3 are still available on the old package name. Further maintenance releases since 0.4.0 will be available only on the package name 'emencia-contact-form-maintenance'. However, this package is in maintenance mode only, there will not be any other fixes or features.**

This is aimed to be a reusable app for our cookiecutter. Django CMS integration is provided.

It add a generic contact form with some basic configuration made available via the admin.


Install
-------

- create your virtualenv and `pip install emencia-contact-form-maintenance`.

- In your `INSTALLED_APPS`, add:

```python
    'modeltranslation',  # translation within models
    ...
    'django.contrib.site',
    'django.contrib.sitemaps',

    'django-countries',  # needed for the CountryField
    'crispy_forms',  # nice looking forms
    'crispy_forms_foundation',
    'captcha',
    'emencia_contact_form',
```

`modeltranslation` should be placed on top of the installed apps.

There is an automatic check which makes sure all of these apps are in INSTALLED_APPS.

- captcha: signup for [recaptcha](https://github.com/praekelt/django-recaptcha) and follow their installation process on their repo. (adding RECAPTCHA_PUBLIC_KEY, RECAPTCHA_PRIVATE_KEY in your settings and so on..)

- Add url(r'^', include('emencia_contact_form.urls')) in your urls.py

- Ensure you're using foundation with crispyforms, in your settings, add:

```python
CRISPY_ALLOWED_TEMPLATE_PACKS = (
    'bootstrap',
    'uni_form',
    'bootstrap3',
    'bootstrap4',
    'foundation-5',
)
CRISPY_TEMPLATE_PACK = 'foundation-5'
```

Configuration
-------------

- Site: in django Admin, rename the site by default. Ensure you have SITE_ID = 1 in your settings.py

- You can then edit the ContactFormSettings in the admin to configure the email.

- EMAIL BACKEND: on success, the contact form send an email. You need to have it configured to have it working properly. [Django Email Backend](https://docs.djangoproject.com/en/1.10/ref/settings/#std:setting-EMAIL_BACKEND)

- sitemaps: A sitemap is available in contact_form/sitemaps.py
Configuration on the django settings and url has to be done. [doc](https://docs.djangoproject.com/en/1.10/ref/contrib/sitemaps/)


TEST & DEV
----------

Install with pip `requirements-dev.txt` then package in development mode.

Run tests with the following command:
`pytest`

To create a new db while running tests: `pytest --create-db`
The default behavior reuse the same db for performance reasons
