# Используем официальный образ Python
FROM python:3.9-slim

# Устанавливаем необходимые библиотеки
RUN pip install pyTelegramBotAPI mysql-connector-python

# Копируем код бота в контейнер
# COPY DataBase.py /app/bot.py

# Задаем рабочую директорию
WORKDIR /app

# Запускаем бот
# CMD ["python", "DataBase.py"]
