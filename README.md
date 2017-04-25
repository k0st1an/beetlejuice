# Beetle Juice

<p align="center">
    <img src="https://cloud.githubusercontent.com/assets/9702154/20746262/1f0b29e4-b6f6-11e6-8b09-72470fea38d8.png" />
</p>

Микросервис по отправке почтовых сообщений через провайреда sendpulse.ru. Под капотом использует [Django](https://www.djangoproject.com/).

## Настройка

Настройки ниже всего навсего пример. Большую часть настрок можно прописать в `settings.py`.

### django-cors-headers

```python
INSTALLED_APPS = [
    ...
    'corsheaders',
    ...
]

MIDDLEWARE = [
    ...
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]

CORS_ORIGIN_WHITELIST = [
    'domain.com',
    'helper.domain2.com',
]
```

В документации описаны другие возможные настройки.

### DB

```python
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
```

### sendpulse

```python
TOKEN = '12345'

SEND_PULSE = {
    'id': 'XXX',
    'secret': 'XXX',
    'from': {'name': 'Beetlejuice', 'email': 'no-reply@email.ru'}
}
```

`id`/`secret` - даёт сам sendpulse.ru. Вожно учесть с каких доменов Вам разрешено отправлять почту.

## API

Есть поддержка отправки писен как внутренним подписчиками, так и внешним клиентам. В последнем случае придеться использовать токен. Доступны следующие роутеры:

- `<domain>/api/v1/sender/internal/` - для отправки внутренним подписчикам. Метод отправки POST, тип данных JSON.
- `<domain>/api/v1/sender/external/` - для отправки внешним клиентам. Метод отправки POST, тип данных JSON.

Примеры запросов ([HTTPie](https://httpie.org/)):

```
$ http post <domain>/api/v1/sender/internal/ < json/send_email_internal.json
...
$ http post <domain>/api/v1/sender/external/ 'Authorization: XXX' < json/send_email_external.json
```

При успешном запросе вернет JSON со статусом `200`:

```json
{
  "status": true
}
```

Если возникли проблемы при отправке сообщения вернет `false` и статус `400`. Если был отправлен кривой JSON вернет статус `400` и JSON в каком поле что не так.
