## Урок 5. Парсинг данных. Scrapy. Начало

### Вариант I
Написать программу, которая собирает входящие письма из своего или тестового почтового ящика и сложить данные о письмах в базу данных (от кого, дата отправки, тема письма, текст письма полный)
Для этого нужно создать свой тестовый почтовый ящик и переслать на него минимум любых рекламных 50 сообщений.

---

### Структура
- main.py - мэин скрипт
- .env - содержит доступы к почте и mongodb

### Запуск
`python main.py` - Запуск сбора писем с почты

### Пример файла .env
```dotenv
email=YOUR_EMAIL
password=YOUR_PASSWORD
DB_NAME=DATABASE_NAME
TABLE_NAME=TABLE_NAME
```

### PS:
По факту это задание из урока по selenium