
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '9@!mp5#sk^hrra4avc)vvc5o0nt-m1z(quxn#&l!^#xyw61_tu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'movie',
    }
}
