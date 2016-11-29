from django.core.checks import Error, register


@register()
def check_modeltranslation_contactform_in_installed_apps(app_configs, **kwargs):
    from django.conf import settings

    errors = []
    needed_modules = ['modeltranslation', 'contact_form', ]

    for module in needed_modules:
        if module not in settings.INSTALLED_APPS:
            errors.append(
                Error(
                    'INSTALLED_APPS is incomplete',
                    hint="Add '{mod}' in your INSTALLED_APPS".format(
                        mod=module),
                    obj='Import Error',
                    id='contact_form.check',
                )
            )
    return errors
