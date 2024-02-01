
=========
Changelog
=========

Version 0.4.0 - 2024/02/01
--------------------------

Due to ownership problems with package on Pypi, we needed to move this package to a new
name ``emencia-contact-form-maintenance``.

Anything have been changed except the package name and the package setup, you should be
able to safely move from 0.3 to this version and further.

So instead of doing: ::

    pip install emencia-contact-form

You will do now: ::

    pip install emencia-contact-form-maintenance

Or update your project requirements in the same way.


Version 0.3.1 - Not released as a package on Pypi
-------------------------------------------------

This is a maintenance release to level up Django support to ``1.11`` since some
projects use it in production althrough the package explicitely limited support to
``Django<1.11``.

Previously with old Pip with old dependencies resolver, project were able to install it
but recent Pip with new resolver was blocked with Django support conflicts, this
maintenance release will solve this and projects will be able to move to recent Pip.


Version 0.3 - 2017/01/12
------------------------

Previous versions did not have any changelog.
