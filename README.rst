Super Duper Beetle Juice
========================

.. image:: https://cloud.githubusercontent.com/assets/9702154/20746262/1f0b29e4-b6f6-11e6-8b09-72470fea38d8.png


requirements
------------

- ``django``
- ``djangorestframework``
- ``django-cors-headers``


todo
----

- Добавить поддержку отпраки через SMTP указанный в экшене (модель реализована)
- Белый список от кого принимать запросы

тестируем
---------

Тестирование::

    http POST http://127.0.0.1:8000/api/v1/send/ < test.json

``http`` - `HTTPie <https://httpie.org/>`_


настройки
---------

Настройки ниже всего навсего пример. Большую часть настрок можно прописать в ``settings.py``.

CORS
^^^^

Для ``django-cors-headers``::

    MIDDLEWARE = [
        ...
        'corsheaders.middleware.CorsMiddleware',
        'django.middleware.common.CommonMiddleware',
        ...
    ]

    CORS_ORIGIN_WHITELIST = [
        'localhost:5000',
    ]

В документации описаны другие возможные настройки.


Email
^^^^^

Нужно указать от кого отправлять письма. Обычно без указания правильного (с точки зрения насроек провайдера предоставляющего доступ к SMTP) обратного адреса отправить письмо не получится. Для этого нужно в ``settings.py`` определить переменную ``EMAIL_FROM``. Ниже пример настройки::

    EMAIL_HOST = 'smtp-pulse.com'
    EMAIL_PORT = 465
    EMAIL_USE_SSL = True
    EMAIL_TIMEOUT = 5
    EMAIL_HOST_USER = 'me@domain.com'
    EMAIL_HOST_PASSWORD = 'JLou2lHHd2jdf32Df'
    EMAIL_FROM = 'example@domain.com'


DB
^^
::

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'DB-NAME',
            'USER': 'DB-USERNAME',
            'PASSWORD': 'DB-PASSWORD',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }

