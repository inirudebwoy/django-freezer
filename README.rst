==============
Django Freezer
==============

Installation
============
Install from cheeseshop.imagination.net::

  easy_install -ZU -i https://cheeseshop:*****@cheeseshop.imagination.net/ djangofreezer

Put package in INSTALLED_APPS.::

  INSTALLED_APPS += ('djangofreezer',)

In urls.py add import of AdminSiteExtended from djangofreezer::

  from djangofreezer.admin import AdminSiteExtended

Next create new extended site before calling autodiscover()::

  admin.site = AdminSiteExtended()

If you are using Django 1.7 and higher than it is necessery to disable autodiscover
as per `https://docs.djangoproject.com/en/1.7/ref/contrib/admin/#django.contrib.admin.autodiscover`_
