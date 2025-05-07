# REEZOLDINI audio Website

Официальный веб-сайт компании REEZOLDINI audio, производителя высококачественной акустики.

## Установка

1. Создайте виртуальное окружение Python:
```bash
python -m venv venv
```

2. Активируйте виртуальное окружение:
```bash
# Windows
venv\Scripts\activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Создайте файл .env в корневой директории проекта:
```
SECRET_KEY=your-secret-key-here
```

5. Инициализируйте базу данных:
```bash
flask db init
flask db migrate
flask db upgrade
```

## Запуск

Для запуска сайта выполните:
```bash
python app.py
```

Сайт будет доступен по адресу: http://localhost:5000

## Структура проекта

- `/static` - Статические файлы (CSS, JavaScript, изображения)
- `/templates` - HTML шаблоны
- `app.py` - Основной файл приложения
- `requirements.txt` - Зависимости проекта

## Функциональность

- Просмотр продукции по категориям
- Форма обратной связи
- Информация о компании
- Адаптивный дизайн
- База данных для хранения информации о продуктах и обращениях
