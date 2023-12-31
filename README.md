# О проекте
Это учебный проект. Он реализует сервис авторизации с системой ролей, написанный на FastAPI, который может быть использован как элемент  онлайн-киносервиса.


# Структура проекта
- Корень проекта — в нём находится всё базовое (Dockerfile, requirements.txt и gitignore).
- src — содержит исходный код приложения.
- main.py — входная точка приложения.
- api — модуль, в котором реализуется API. Другими словами, это модуль для предоставления http-интерфейса клиентским приложениям. Внутри модуля отсутствует какая-либо бизнес-логика, так как она не должна быть завязана на HTTP.
- core — содержит разные конфигурационные файлы.
- db — предоставляет объекты баз данных (Redis, PostgreSQL) и провайдеры для внедрения зависимостей.
- models — содержит классы, описывающие бизнес-сущности и модели базы данных.
- services — главное в сервисе: здесь находится реализация всей бизнес-логики.


## Архитектура (заметки)
Для хранения данных пользователей и истории входов используется PostgreSQL.


# Разработка

## Установка и запуск

### Создание пользователя, базы данных и схемы Postgres
Для упрощения на этапе разработке предлагается использовать локально установленный Postgres.
Необходимо вручную создать пользователя Postgres, базу данных и схему, с которыми будет работать FastAPI.
Подключение к PostgreSQL:
```
psql -U postgres -h 127.0.0.1
```

Создание пользователя:
```
CREATE ROLE user WITH LOGIN PASSWORD 'password';
```

Наделение пользователя правом создавать базы данных и выход из консоли PostgreSQL:

```
ALTER ROLE user CREATEDB;
\q
```

Подключение под новым пользователем:
```
psql postgres -U user
```

Создание базы данных:
```
CREATE DATABASE database;
```

Подключение к новой базе данных и создание схемы:
```
\connect authapi_database
CREATE SCHEMA schema;
```

### Переменные окружения
После клонирования проекта создайте файл с переменными окружения '.env' в корне проекта.
Шаблон с именами переменных находится в корне репозитория и имеет название: '.env.example'.

### Запуск сервера

```
uvicorn main:app --reload
```

В этой команде:
- uvicorn - команда для запуска сервера uvicorn.
- main:app - ссылка на приложение FastAPI.
- --reload - опциональный флаг, который автоматически перезапускает сервер при обнаружении изменений в исходном коде. Только для разработки, не следует использовать в продакшене.

В момент запуска(`@app.on_event('startup')`) SQLAlchemy будет пытаться создать все таблицы (`async def startup()`), которые ещё не существуют в базе данных. Существующие таблицы или данные затронуты не будут.




