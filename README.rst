==============
Django Freezer
==============

Installation
============

Put package in INSTALLED_APPS.
In urls.py add import of admin_site from freezer

from djangofreezer.admin import AdminSiteExtended

Next add
admin.site = AdminSiteExtended
before calling autodiscover()
