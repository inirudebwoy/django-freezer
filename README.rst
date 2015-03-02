==============
Django Freezer
==============

Installation
============

Put package in INSTALLED_APPS.
In urls.py add import of admin_site from freezer

from imagination.freezer.admin import admin_site

Next add
admin.site = admin_site
before calling autodiscover()
