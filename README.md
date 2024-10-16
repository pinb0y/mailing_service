## Сервис для массовой рассылки !ТУРБО СПАММЕР СРИ САУЗЕНТ!
Автоматически рассылает писма на указыанные адреса по расписанию(ежедневно, еженедельно, ежемесячно)

[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Postgresql](https://img.shields.io/badge/-Postgresql-464646?style=flat-square&logo=Postgresql)](https://www.postgresql.org/)
[![Redis](https://img.shields.io/badge/-Redis-464646?style=flat-square&logo=Redis)](https://redis.io/)


### Технологии:
- python 3.12.4
- django 4.2
- pillow 10.4.0
- psycopg2-binary 2.9.9
- pytils 0.4.1
- redis 5.1.1
- black 24.10.0

# Инструкция по запуску

### 1 шаг. Склонируйте проект

### 2 шаг. Установите все зависмости командой poetry install

### 3 шаг. Переименуйте файл .envsample в .env и добавьте в него все необходимые настройки по шаблону.

### 4 шаг. Добавьте в crontab переодические задачи командой crontab -e  

\* \* \* \* \* /путь до интерпритатора/python /путь до папки с проектом/manage.py search_mailings
          
50 23 * * * /путь до интерпритатора/python /путь до папки с проектом/manage.py day  

50 23 * * 5 /путь до интерпритатора/python /путь до папки с проектом/manage.py week  

50 23 1 * * /путь до интерпритатора/python /путь до папки с проектом/manage.py month  

### 5 шаг. Запустите сервер с приложением командой python manage.py runserver 

### 6 шаг. Перейдите по адресу из командной строки и кайфуйте! 

Автор проекта Пинчук Сергей
