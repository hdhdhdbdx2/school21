# Запуск Лавки

Профиль правил: E2

В одном заказе разрешено не больше двух единиц. Персональный лимит на общее количество сохраняется.

Все команды выполняются из папки с `RUN.md`.

## Подготовить окружение

Для первого запуска с Python 3.12 или новее установите зависимости в локальное окружение.

~~~bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r materials/requirements.txt -c materials/requirements-campus.lock.txt
python3 check_environment.py
~~~

Если кампусное окружение уже подготовлено, активируйте его по `materials/environment_rus.md` и выполните `python3 check_environment.py`. В новом терминале повторите активацию.

## Запустить демонстрацию

~~~bash
python3 client.py demo
~~~

## Пройти полный сценарий

~~~bash
python3 client.py scenario
~~~

## Запустить сервер для другого клиента

~~~bash
python3 -m src.server
~~~

Транспорт — stdio. Сам сервер ждёт сообщения клиента; видимый сценарий запускается через client.py.

## Проверить проект

~~~bash
python3 -m pytest -q
python3 checks/acceptance.py --project . --profile E2
~~~

## Состояние

Ручные запросы `client.py call` и прямой запуск сервера используют data/lavka.db. Перезапуск сохраняет эту базу.

Команды demo и scenario без --db каждый раз создают временную базу и удаляют её после завершения. Для сохранения результата сценария задайте --db, как в примере ниже.
Журнал клиента: logs/client.jsonl.

Чтобы получить чистую базу и сохранить результат отдельно, укажите новый путь. Команды ниже создают для неё уникальную временную папку.

~~~bash
lavka_trial="$(mktemp -d)"
python3 client.py --db "$lavka_trial/trial.db" scenario
~~~

Если указанный файл уже существует, клиент продолжит работу с его состоянием. Журнал записывает аргументы и ответы, а состояние заказов, балансов и остатков хранится в SQLite.

## Наш пример запроса

~~~bash
python3 client.py call get_product '{"product_id":"hoodie"}'
~~~

На свежей базе клиент получил следующий ответ.

~~~json
{
  "ok": true,
  "data": {
    "id": "hoodie",
    "name": "Худи",
    "price_coins": 500,
    "user_limit": 1,
    "stock": {"L": 2, "M": 5, "S": 3, "XL": 1}
  }
}
~~~

В ответе видны цена в коинах, лимит на участника и остаток каждого размера. Запись об этом вызове появляется в `logs/client.jsonl`.

