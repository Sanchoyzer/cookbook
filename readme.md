## Описание

Кулинарная книга


## Технологии

python 3.7, Django, DRF, sqlite, docker


## Установка

0. Убедиться, что есть docker

1. Создать конфиг в .env файле рядом с settings.py

```csv
SECRET_KEY='jber8h43gljn394njb-3ph0'
DEBUG='false'
ALLOWED_HOSTS='127.0.0.1,0.0.0.0'
```

2. Собрать образ и запустить контейнер

```commandline
docker image rm cookbook:1.0
docker image build -t cookbook:1.0 .
docker container run -it -p 12345:12345 -v /my_project/sites/db.sqlite3:/srv/src/sites/db.sqlite3 --rm cookbook:1.0
```


## API

### Получить рецепты, которые можно приготовить

**Request**

    GET /api/v1/cookbook/what_can_i_cook/
    
    params: ingredient=count
    
**Response**

    HTTP/1.1 200 OK
    Content-Type: application/json
    
    {
        "data": {
            recipe_name (str): portions_count (int),
            ...
        }
    }


#### Пример

**Request**

    GET /api/v1/cookbook/what_can_i_cook/?мясо=750&огурец=10&картофель=12
    
**Response**

    HTTP/1.1 200 OK
    Content-Type: application/json
    
    {
        "data": {
            "Салат «Ленинградский»": 1,
            "Салат «Русский»": 3
        }
    }
