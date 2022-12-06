REST API социальной сети YaTube (Яндекс.Практикум)
Описание проекта

Проект создан в рамках учебного курса Яндекс.Практикум.

API сервис для проекта социальной сети Yatube.

Реализован REST API CRUD для основных моделей проекта, для аутентификации примненяются JWT-токены. В проекте реализованы пермишены, фильтрации, сортировки и поиск по запросам клиентов, реализована пагинация ответов от API, установлено ограничение количества запросов к API.

Стек технологий

    Python 3.7
    Django 2.2
    Django Rest Framework
    Pytest
    Simple-JWT
    SQLite3

Установка проекта из репозитория (Linux и macOS)

    Клонировать репозиторий и перейти в него в командной строке:

git clone git@github.com:vlad3069/api_final_yatube.git

cd API_YaTube

    Cоздать и активировать виртуальное окружение:

python3 -m venv env

source env/bin/activate

    Установить зависимости из файла requirements.txt:

python3 -m pip install --upgrade pip

pip install -r requirements.txt

    Выполнить миграции:

cd yatube_api

python3 manage.py migrate

    Запустить проект (в режиме сервера Django):

python3 manage.py runserver

Документация к проекту

Документация для API после установки доступна по адресу /redoc/.