# Beetle Juice

<p align="center">
    <img src="https://cloud.githubusercontent.com/assets/9702154/20746262/1f0b29e4-b6f6-11e6-8b09-72470fea38d8.png" />
</p>

Микросервис по отправке почтовых сообщений через провайреда sendpulse.ru.

## TODO

- Добавить поддержку отпраки через SMTP указанный в экшене (модель реализована)
- Белый список от кого принимать запросы

## Тестируем

```
http POST http://127.0.0.1:8000/api/send/ < test.json
```

`http` - [HTTPie](https://httpie.org/).


## Настройки

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


### Email

Нужно указать от кого отправлять письма. Обычно без указания правильного (с точки зрения настроек провайдера предоставляющего доступ к SMTP) обратного адреса отправить письмо не получится. Для этого нужно в `settings.py` определить переменную `EMAIL_FROM`. Ниже пример настройки:

```python
EMAIL_HOST = 'smtp-pulse.com'
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_TIMEOUT = 5
EMAIL_HOST_USER = 'me@domain.com'
EMAIL_HOST_PASSWORD = 'JLou2lHHd2jdf32Df'
EMAIL_FROM = 'example@domain.com'
```

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

## Sender

На данный момент проект переписывается для работы с провайдером через его REST API. Предпологается, что будет два типа отправки писем: как сейчас, используя `action` и отправка внешним получателя. В последнем случае придется использовать токен.

Для работы нужно добавить в конфиг `settings.py` следующее:

```python
TOKEN = '12345'

SEND_PULSE = {
    'id': '67890',
    'secret': '101010',
    'from': {'name': 'Beetlejuice', 'email': 'no-reply@email.ru'}
}
```

`id`/`secret` - даёт сам sendpulse.ru. После этого можно отправлять POST запрос на URL `https://<domain>/api/v1/sender/external/` с залоговком `Authorization` в формате JSON. Пример заголовка:

```
Authorization: test
```

Пример JSON можно найти в файле `json/send_email.json`. Полный пример:

```bash
$ http post https://<domain>/api/v1/sender/external/ 'Authorization: test' < json/send_email.json
```

Пока `sender` в зачаточном состоянии...
