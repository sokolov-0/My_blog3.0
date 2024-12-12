from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-($c*!4%gr@1ba_@cky@s$b@48&y7(_jtv%9u_95*mbn@+ofmsk'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


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
    #'django.core.paginator',
    'mozilla_django_oidc',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'mozilla_django_oidc.middleware.SessionRefresh',
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

LOGIN_URL = 'accounts:oidc_login'#регистрация 
# Основные настройки OIDC
OIDC_RP_CLIENT_ID = "django-app"  # ID клиента, созданного в Keycloak
OIDC_RP_CLIENT_SECRET = 'txFEbWAn7OKM2Wf1oi6c6t43cNBkaqoQ' # Секрет клиента из Keycloak 
OIDC_OP_AUTHORIZATION_ENDPOINT = "http://localhost:8080/realms/blog/protocol/openid-connect/auth"
OIDC_OP_TOKEN_ENDPOINT = "http://localhost:8080/realms/blog/protocol/openid-connect/token"
OIDC_OP_USER_ENDPOINT = "http://localhost:8080/realms/blog/protocol/openid-connect/userinfo"
OIDC_OP_JWKS_ENDPOINT = "http://localhost:8080/realms/blog/protocol/openid-connect/certs"

OIDC_RP_SIGN_ALGO = "RS256"  # Алгоритм подписи

OIDC_AUTHENTICATION_CALLBACK_URL = "http://localhost:8000/accounts/oidc/callback/"
 # Путь на который будет отправлен пользователь после успешной аутентификации



OIDC_RENEW_ID_TOKEN_EXPIRY_SECONDS = 600 #обновление токена
# URL-адреса для перенаправления после входа и выхода
LOGIN_REDIRECT_URL = 'http://localhost:8000/'
LOGOUT_REDIRECT_URL = 'http://localhost:8000/'

OIDC_CREATE_USER = True
OIDC_USERNAME_FIELD = 'preferred_username'

OIDC_RP_SCOPES = 'openid email profile'

AUTH_USER_MODEL = 'accounts.CustomUser'




MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


