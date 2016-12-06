# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.forms import ModelForm

from captcha.fields import ReCaptchaField

from .forms_utils import create_basic_form_helper
from .mails import send_mail_to_contact
from .models import Contact


class ContactForm(ModelForm):
    error_css_class = 'error'
    required_css_class = 'required'

    captcha = ReCaptchaField(attrs={'theme': 'clean'})

    class Meta:
        model = Contact
        fields = ('civility', 'first_name', 'last_name', 'email', 'message',
                  'phone', 'company', 'city', 'state', 'country',
                  'optin_newsletter', 'captcha', )

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.helper = create_basic_form_helper()

    def save(self, commit=True):
        contact = super(ContactForm, self).save()
        send_mail_to_contact(contact)
        return contact
