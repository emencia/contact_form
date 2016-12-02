# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _


MRS = "mrs"
MR = "mr"


CIVILITY_CHOICES = (
    (MRS, _('Mrs')),
    (MR, _('Mr')),
)


CIVILITY_DICT = dict(CIVILITY_CHOICES)
