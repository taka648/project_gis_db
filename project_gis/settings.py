# import
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-gl)=4*(hsv-p3kd^r)g=k%olj6t&+)4ovy9^g4z_0k1ck78*+$"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "datashare",                  # 3.2.3 Djangoアプリの登録
    "account.apps.AccountConfig", # リスト4-25:追加。4.6.1 ユーザ認証のテスト実装、手順1:アプリケーションaccountの登録
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project_gis.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        #"DIRS": [],
        "DIRS": {os.path.join(BASE_DIR, 'templates')}, # リスト4-26:修正。4.6.1 ユーザ認証のテスト実装、手順2:その他の修正と追加設定
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # "django.template.context-processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project_gis.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

# DATABASES = {
#    "default": {
#        "ENGINE": "django.db.backends.sqlite3",
#        "NAME": BASE_DIR / "db.sqlite3",
#    }
# }
# リスト4-2:projcct_gis/settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "project_gis_db",
        "USER": "taka648",
        "PASSWORD": "Akie2Suzuki",
        "PORT": "5432",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

# LANGUAGE_CODE = "en-us"
# TIME_ZONE = "UTC"
# 4.4.3 モデルのデータベース実装、手順1:必要な環境設定、(B)アプリの言語と時間の環境設定する。
LANGUAGE_COOE = "ja"  # リスト4-8:修正
TIME_ZONE = "Asia/Tokyo"  # リスト4-8:修正

USE_I18N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

# 4.6.2 アプリケーションdatashareにおけるユーザ認証機能の実装、手順5:
# project_gis/settings.pyに設定した[LOGIN_URL]と[LOGIN_REDIRECT_URL]を、それぞれ[datashare:login]と[datashare:mypage_db]に変更する。
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# 4.4.3 モデルのデータベース実装、手順1:必要な環境設定、(B)アプリのアップロードファイル保存先に関する環境設定
MEDIA_URL = "/media/"                         # リスト4-8:追加
MEDIA_ROOT = os.path.join(BASE_DIR, "media")  # リスト4-8:追加
# 4.6.1 ユーザ認証のテスト実装、手順2:その他の修正と追加設定
LOGIN_URL = "account:login"          # リスト4-27:追加
# LOGIN_REDIRECT_URL = 'account:top' # リスト4-27:追加
LOGIN_REDIRECT_URL = "datashare:mypage_db" #リスト4-42:追加

