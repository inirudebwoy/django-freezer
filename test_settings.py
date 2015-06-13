INSTALLED_APPS = (
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.messages',
    'django.contrib.auth',
    'django.contrib.admin',
    'django_freezer',
)

SECRET_KEY = 'djangofreezer'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'test.db',
    },
}

MIDDLEWARE_CLASSES = ()
