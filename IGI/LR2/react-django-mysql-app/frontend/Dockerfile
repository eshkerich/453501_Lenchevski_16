# Этап сборки
FROM node:18-alpine AS build

WORKDIR /app

# Копирование package.json и package-lock.json
COPY package*.json ./

# Установка зависимостей
RUN npm install

# Копирование исходного кода
COPY . .

# Сборка приложения
RUN npm run build

# Этап production
FROM nginx:stable-alpine

# Копирование собранных файлов
COPY --from=build /app/build /usr/share/nginx/html

# Копирование конфигурации nginx
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]