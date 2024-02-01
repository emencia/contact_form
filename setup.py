from setuptools import setup, find_packages

setup(
    name='emencia-contact-form-maintenance',
    version=__import__('emencia_contact_form').__version__,
    description=__import__('emencia_contact_form').__doc__,
    long_description=open('README.md').read(),
    author='Emencia',
    author_email='support@emencia.com',
    url='https://github.com/emencia/contact_form',
    license='AGPL 3.0',
    packages=find_packages(),
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.10',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'django>=1.8,<2.0',
        'django-modeltranslation',
        'django-countries',
        'django-crispy-forms'
        'crispy-forms-foundation',
        'django-recaptcha',
        'django-import-export',
        'django-cms>=3',
        # used in hierarchy for ContactAdmin
        'pytz',
    ],
)
