# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Запуск
Команда для установки зависимостей:
``` 
pip install -r requirements.txt
``` 

Сайт берет данные из файла: `wines.xlsx`. Путь до этого файла необходимо задать в переменной 
окружения, в файле `.env`.
```
PATH_TO_EXEL_FILE=
```

Пример заполнения таблицы в `wines.xlsx`:

| Категория | Название | Сорт | Цена | Картинка   | Акция                |
|-----------|----------|------|------|------------|----------------------|
| Напитки   | Чача     |      | 299  | chacha.png | Выгодное предложение |
| ...       |          |      |      |            |                      |

Команда для локального запуска сайта:
``` 
python main.py
```
Откройте сайт в браузере по адресу http://127.0.0.1:8000/

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
