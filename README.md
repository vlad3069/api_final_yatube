# Проект API Yatube

API сервис для проекта социальной сети Yatube

## Описание

Проект для публикации блогов. Позволяет отправлять записи в сообщества и просматривать там записи других авторов. Имеется возможность модерировать записи и блокировать пользователей.

## Реализован

* REST API CRUD для основных моделей проекта
* JWT-токены для аутентификации  
* пермишены, фильтрации, сортировки и поиск по запросам клиентов
* пагинация ответов от API
* установлено ограничение количества запросов к API.

## Технологии

* Python 3.7
* Django 2.2.19
* Django Rest Framework
* Pytest
* Simple-JWT
* SQLite3

## Начало работы

* Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:vlad3069/api_final_yatube.git

cd API_YaTube

* Cоздать и активировать виртуальное окружение:

python3 -m venv env

source env/bin/activate

* Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip

pip install -r requirements.txt

* Выполнить миграции:

cd yatube_api

python3 manage.py migrate

* Запустить проект (в режиме сервера Django):

python3 manage.py runserver

## Документация к проекту

Документация для API после установки доступна по адресу http://localhost/api/docs/redoc.html.
