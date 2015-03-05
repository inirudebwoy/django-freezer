#  -*- coding: utf-8 -*-
import djangofreezer

try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup


setup(
    name='djangofreezer',
    version=djangofreezer.__version__,
    description='Print pip freeze in your admin panel',
    author='Michal Klich',
    author_email='michal.klich@imagination.com',
    include_package_data=True,
    packages=['djangofreezer'],
    url='https://bitbucket.org/michalklich/django-freezer',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Framework :: Django',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
