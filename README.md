# Как запустить проект?

## 1. Установка poetry

```sh
pip install poetry
```

## 2. Установка зависимостей

```sh
poetry lock && poetry install && poetry shell
```

## 3. Миграции

```sh
./manage.py migrate
```

## 4. Запуск проект

```sh
./manage.py runserver
```
