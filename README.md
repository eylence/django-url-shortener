#### Django URL Shortener with Django REST framework

##### Installation

`git clone https://github.com/eylence/django-url-shortener.git`

`pip install -r requirements.txt`

`python manage.py migrate`

`python manage.py runserver`

##### Sample Request & Response
```shell
~$ curl -d '{"url": "https://www.youtube.com/watch?v=u_LAG1RQkCs"}' -H "Content-Type: application/json" -X POST http://127.0.0.1:8000/shorten/
```

```json
{
    "url":"https://www.youtube.com/watch?v=u_LAG1RQkCs",
    "shortened_url":"https://SHORTURL/4rGjQR"
}
```

```shell
~$ curl -sI http://127.0.0.1:8000/4rGjQR | grep Location
Location: https://www.youtube.com/watch?v=u_LAG1RQkCs
```