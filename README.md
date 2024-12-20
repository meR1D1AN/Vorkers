# Микросервис для работников

Этот проект представляет собой микросервис для управления работниками. Он предоставляет API для выполнения операций CRUD (создание, чтение, обновление и удаление) для работников.

## Установка и запуск

Для запуска проекта используйте `docker-compose`. Следуйте этим шагам:

1. Скопируйте файл `.env.sample` в `.env`:
   ```bash
   cp .env.sample .env
   ```

2. Введите необходимые данные в файл .env.

3. Запустите проект с помощью docker-compose:
   ```bash
   docker-compose up -d --build
   ```

## Использование

Чтобы узнать, какие эндпоинты доступны, перейдите по следующему адресу в вашем браузере:

http://127.0.0.1/api/v1/swagger/


### API Эндпоинты
#### Работники
- GET /workers/: Получение списка всех работников.
- GET /team/{team_id}/workers/: Получение списка работников в бригаде.
- POST /workers/: Создание нового работника.
- GET /workers/{id}/: Получение детальной информации о работнике.
- PUT /workers/{id}/: Обновление информации о работнике.
- PATCH /workers/{id}/: Частичное обновление информации о работнике.
- DELETE /workers/{id}/: Удаление работника.

## Тесты в контейнере

```bash 
    docker-compose exec app bash python3 manage.py test
```

# Что можно улучшить

- В новой ветке добавить создание дополнительных приложений, к примеру расчёт зарплаты за выполненные работы. Дополнительно добавить график работы сотрудников, чтобы к примеру иметь стандартную ставку сотрудника, и дополнительно доплачивать ему за выполненный объём. (эту возможность смогу добавить, если она покажется нужной, я её делал уже, дополнительно еще формировался excel документ с графиком для подписи)
- Так как это микросервис, я предполагаю, что у него уже есть авторизация и аутентификация. Аутентификацию сделал через JWT. 


### Ожидаю результата. Контакты: Telegram: @mered1an