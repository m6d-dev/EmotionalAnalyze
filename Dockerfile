# Используем официальный Python 3.10 образ
FROM python:3.10-slim

# Устанавливаем зависимости для DeepFace и Pillow
RUN apt-get update && apt-get install -y \
    libgl1 \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта
COPY . /app

# Устанавливаем зависимости Python
RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Применяем миграции (можно закомментировать, если миграции отдельно)
RUN python manage.py migrate

# Прокидываем порт
EXPOSE 8000

# Команда запуска Django сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
