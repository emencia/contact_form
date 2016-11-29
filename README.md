Contact Form App
================

This is aimed to be a reusable app for our cookiecutter.
It add a generic contact form with some basic configuration made available via django-constance.


Install
-------

- For django-constance, you'll need Redis setup and running.

- Add url(r'^', include('contact_form.urls')) in your urls.py

- In your `INSTALLED_APPS`, add `'contact_form'` and `'modeltranslation'`.
`modeltranslation` should be placed on top of the installed apps.

There is an automatic check which makes sure both of these apps are in INSTALLED_APPS.


TEST & DEV
----------

There is requirements-dev.txt with pdb, django-extensions and pygraphviz.

Run tests with the following command:
`pytest`

To create a new db while running tests: `pytest --create-db`
The default behavior reuse the same db for performance reasons
