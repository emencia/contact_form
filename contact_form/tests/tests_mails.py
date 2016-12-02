# -*- coding: utf-8 -*-

import pytest

from django.test import SimpleTestCase

from ..mails import send_mail_to_contact, remove_all_newlines
from ..models import Contact


class TestMail(SimpleTestCase):
    def test_remove_all_newlines(self):
        string_test = '\r\n foo \n\t\r\n \n\n\r\n\r\rbar'
        expected = '  foo  \t       bar'
        assert expected == remove_all_newlines(string_test)


@pytest.mark.django_db
def test_send_mail_to_contact(mocker):
    contact = Contact(first_name="foo", last_name="bar")

    mock = mocker.patch('contact_form.mails.send_mail')
    assert not mock.called

    send_mail_to_contact(contact)
    assert mock.called
