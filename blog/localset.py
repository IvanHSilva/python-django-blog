DEBUG = False
ALLOWED_HOSTS = ['35.215.212.158', 'localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'IvanHS',
        'PASSWORD': 'IvanHS@123*',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}

SECURE_PROXY_SSL_HEADER = None
SECURE_SSL_REDIRECT = None
SESSION_COOKIE_SECURE = None
CSRF_COOKIE_SECURE = None
