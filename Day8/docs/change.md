# Конверт E5

Сдаваемый профиль: E5

## Условие

Вариант E5 «Худи по предварительному заказу» из `envelopes/E5.md`. Ветку используют, если платформа выдала этот конверт.

Созданный заказ худи можно выдать. Попытка его отменить возвращает `ORDER_STATUS_ERROR`. В base созданный заказ худи отменяется. В E5 баланс, остаток и статус после отказа сохраняются. Созданный заказ бутылки можно отменить.

## До изменения

В `src/domain.py` нужно поменять `can_cancel`. В `testing/test_orders.py` нужен тест нового правила. В описании `cancel_order` в `contracts/tools_schemas.json` нужно предупредить клиента о новом поведении. Профиль и правило надо записать в инструкции и паспорте.

## Что сделано

Изменил правило в `src/domain.py`, уточнил описание инструмента и выставил профиль E5 в инструкции и паспорте. Новое поведение проверяет `test_hoodie_cannot_be_cancelled` и `test_bottle_can_still_be_cancelled` в `testing/test_orders.py`.

## Проверка

```bash
python3 -m pytest -q testing/test_example.py testing/test_orders.py
python3 checks/acceptance.py --project . --profile E5
```

Прошло тестов pytest — 8. Итог приёмки — `PASS — профиль E5, вызовов инструментов: 49`.
