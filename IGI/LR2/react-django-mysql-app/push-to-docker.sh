DOCKER_USERNAME="truevamp"
VERSION="1.0"

# Найдите ID образов
docker images

# Backend
docker tag react-django-mysql-app-backend:latest ${DOCKER_USERNAME}/react-django-backend:${VERSION}
docker tag react-django-mysql-app-backend:latest ${DOCKER_USERNAME}/react-django-backend:latest
docker push ${DOCKER_USERNAME}/react-django-backend:${VERSION}
docker push ${DOCKER_USERNAME}/react-django-backend:latest

# Frontend
docker tag react-django-mysql-app-frontend:latest ${DOCKER_USERNAME}/react-django-frontend:${VERSION}
docker tag react-django-mysql-app-frontend:latest ${DOCKER_USERNAME}/react-django-frontend:latest
docker push ${DOCKER_USERNAME}/react-django-frontend:${VERSION}
docker push ${DOCKER_USERNAME}/react-django-frontend:latest