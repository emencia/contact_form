from django.test import SimpleTestCase
from django.test.utils import isolate_apps

from ..checks import check_modeltranslation_contactform_in_installed_apps


@isolate_apps('contact_form', attr_name='apps')
class TestCheck(SimpleTestCase):
    def test_check_installed_app(self):
        with self.settings(INSTALLED_APPS=('django.contrib.admin',)):
            assert len(
                check_modeltranslation_contactform_in_installed_apps(
                    app_configs=self.apps.get_app_configs())
            ) == 2

        assert len(
            check_modeltranslation_contactform_in_installed_apps(
                app_configs=self.apps.get_app_configs())
        ) == 0