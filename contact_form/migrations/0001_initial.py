# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-28 09:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('civility', models.CharField(blank=True, choices=[('mrs', 'Mrs'), ('mr', 'Mr')], max_length=10, verbose_name='Civility')),
                ('first_name', models.CharField(blank=True, max_length=50, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=50, verbose_name='Last Name')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='phone')),
                ('company', models.CharField(blank=True, max_length=255, verbose_name='company')),
                ('city', models.CharField(blank=True, max_length=255, verbose_name='city')),
                ('state', models.CharField(blank=True, max_length=255, verbose_name='state/province')),
                ('country', django_countries.fields.CountryField(blank=True, max_length=2, verbose_name='Country')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('message', models.TextField(blank=True, verbose_name='Message')),
                ('optin_newsletter', models.BooleanField(default=False, verbose_name='Do you wish to receive the newsletter?')),
            ],
            options={
                'verbose_name_plural': 'Contacts',
                'verbose_name': 'Contact',
            },
        ),
        migrations.CreateModel(
            name='ContactFormSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(default='Contact Request', help_text='Email subject for the contact form.', max_length=255, verbose_name='Subject')),
                ('subject_en', models.CharField(default='Contact Request', help_text='Email subject for the contact form.', max_length=255, null=True, verbose_name='Subject')),
                ('subject_fr', models.CharField(default='Contact Request', help_text='Email subject for the contact form.', max_length=255, null=True, verbose_name='Subject')),
                ('email_to', models.TextField(default='example@example.com', help_text='You can specify multiple mail address.', verbose_name='Send mail to')),
                ('email_from', models.EmailField(default='do_not_answer@emencia.com', max_length=254, verbose_name='Send contact email as')),
                ('success_html', models.TextField(default='<h2>Success</h2>\n<p>Thank you for your message, we will get back to you quickly !</p>', verbose_name='Success Message (in html)')),
                ('success_html_en', models.TextField(default='<h2>Success</h2>\n<p>Thank you for your message, we will get back to you quickly !</p>', null=True, verbose_name='Success Message (in html)')),
                ('success_html_fr', models.TextField(default='<h2>Success</h2>\n<p>Thank you for your message, we will get back to you quickly !</p>', null=True, verbose_name='Success Message (in html)')),
                ('site', models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
            options={
                'verbose_name_plural': 'Contact Form Settings',
                'verbose_name': 'Contact Form Settings',
            },
        ),
    ]
