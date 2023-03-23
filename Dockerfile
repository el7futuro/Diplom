# Базовый образ Python (в нем уже установлен Python, pip и прочее)
FROM python:3.10-slim

# Создаем директорию /app и переходим в нее
WORKDIR app/
# Копируем файл с зависимостями
COPY requirements.txt .
# Устанавливаем через pip зависимости
RUN pip install -r requirements.txt
# Копируем код приложения
COPY . .
# Копируем код приложения

# Указываем команду, которая будет запущена командой docker run
CMD python manage.py runserver 0.0.0.0:8000
