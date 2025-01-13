from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-($c*!4%gr@1ba_@cky@s$b@48&y7(_jtv%9u_95*mbn@+ofmsk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

CSRF_TRUSTED_ORIGINS = ['http://localhost:8000', 'http://localhost:8080']
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app.blog_app',
    'app.accounts',
    'django_keycloak',
    'django_extensions',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_keycloak.middleware.BaseKeycloakMiddleware',  # Middleware для Keycloak
    'django_keycloak.middleware.RemoteUserAuthenticationMiddleware',  # Middleware для авторизации
]

ROOT_URLCONF = 'blog.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog.wsgi.application'



# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Основные параметры Keycloak
KEYCLOAK_OIDC_PROFILE_MODEL = 'django_keycloak.OpenIdConnectProfile'
KEYCLOAK_SERVER_URL = 'http://localhost:8080'

KEYCLOAK_REALM = 'blog'
KEYCLOAK_CLIENT_ID = 'django-app'
KEYCLOAK_CLIENT_SECRET_KEY = 'txFEbWAn7OKM2Wf1oi6c6t43cNBkaqoQ'

KEYCLOAK_AUTHORIZATION_URL = 'http://localhost:8080/realms/blog/protocol/openid-connect/auth'
KEYCLOAK_TOKEN_URL = 'http://localhost:8080/realms/blog/protocol/openid-connect/token'
KEYCLOAK_USERINFO_URL = 'http://localhost:8080/realms/blog/protocol/openid-connect/userinfo'
KEYCLOAK_END_SESSION_URL ='http://localhost:8080/realms/blog/protocol/openid-connect/logout'
KEYCLOAK_AUTHORIZATION_CONFIG = {
    "SSL_REQUIRED": False,
    "VERIFY_SSL": False,
}

# AUTHENTICATION_BACKENDS = [
#     'django_keycloak.auth.backends.KeycloakAuthorizationBackend',  # Основной бэкенд для аутентификации
#     'django.contrib.auth.backends.ModelBackend',  # Стандартный бэкенд Django (если нужно)
# ]


# URL-адреса для входа и выхода
LOGIN_URL = '/keycloak/login/'
LOGIN_REDIRECT_URL = 'http://localhost:8000/'
LOGOUT_REDIRECT_URL = 'http://localhost:8000/'




#AUTH_USER_MODEL = 'django_keycloak.KeycloakUser'
AUTH_USER_MODEL = 'auth.User'



STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'



