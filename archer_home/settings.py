DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(SITE_ROOT, '..', 'cookbook.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

DATABASE_ROUTERS = ['archer_home.router.

TIME_ZONE = 'Europe/Berlin'

LANGUAGE_CODE = 'de'

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT, '..', 'templates'),
)
