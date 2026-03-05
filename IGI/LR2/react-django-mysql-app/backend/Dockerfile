FROM python:3.9-slim

WORKDIR /app

# Установка системных зависимостей
RUN apt-get update && apt-get install -y \
    gcc \
    default-libmysqlclient-dev \
    pkg-config \
    netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

# Копирование и установка зависимостей Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копирование проекта
COPY . .

# Создание скрипта ожидания базы данных
RUN echo '#!/bin/sh\n\
echo "Waiting for database..."\n\
while ! nc -z $DB_HOST $DB_PORT; do\n\
  sleep 1\n\
done\n\
echo "Database is ready!"\n\
exec "$@"' > /wait-for-db.sh && chmod +x /wait-for-db.sh

EXPOSE 8000

CMD ["/wait-for-db.sh", "python", "manage.py", "runserver", "0.0.0.0:8000"]