#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}ТЕСТ СВЯЗИ МЕЖДУ КОНТЕЙНЕРАМИ${NC}"
echo -e "${BLUE}========================================${NC}"

# Тест 1: Frontend -> Backend
echo -e "\n${YELLOW}Тест 1: Frontend -> Backend${NC}"
if docker exec react_frontend_16 ping -c 2 django_backend_16 > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Frontend успешно пингует Backend${NC}"
    docker exec react_frontend_16 ping -c 2 django_backend_16 | grep "64 bytes"
else
    echo -e "${RED}✗ Frontend НЕ пингует Backend${NC}"
fi

# Тест 2: Backend -> Database
echo -e "\n${YELLOW}Тест 2: Backend -> Database${NC}"
if docker exec django_backend_16 ping -c 2 mysql_db_16 > /dev/null 2>&1; then
    echo -e "${GREEN}✓ Backend успешно пингует Database${NC}"
    docker exec django_backend_16 ping -c 2 mysql_db_16 | grep "64 bytes"
else
    echo -e "${RED}✗ Backend НЕ пингует Database${NC}"
fi

# Тест 3: phpMyAdmin -> Database
echo -e "\n${YELLOW}Тест 3: phpMyAdmin -> Database${NC}"
if docker exec phpmyadmin_16 ping -c 2 mysql_db_16 > /dev/null 2>&1; then
    echo -e "${GREEN}✓ phpMyAdmin успешно пингует Database${NC}"
    docker exec phpmyadmin_16 ping -c 2 mysql_db_16 | grep "64 bytes"
else
    echo -e "${RED}✗ phpMyAdmin НЕ пингует Database${NC}"
fi

# Тест 4: Проверка доступа к API извне
echo -e "\n${YELLOW}Тест 4: Доступ к API из браузера${NC}"
if curl -s http://localhost:8000/api/items/ > /dev/null; then
    echo -e "${GREEN}✓ API доступен по порту 8000${NC}"
    curl -s http://localhost:8000/api/items/ | head -c 100
    echo "..."
else
    echo -e "${RED}✗ API НЕ доступен${NC}"
fi

# Тест 5: Доступ к Frontend из браузера
echo -e "\n${YELLOW}Тест 5: Доступ к Frontend из браузера${NC}"
if curl -s -I http://localhost:3000 | grep "200 OK" > /dev/null; then
    echo -e "${GREEN}✓ Frontend доступен по порту 3000${NC}"
else
    echo -e "${RED}✗ Frontend НЕ доступен${NC}"
fi

echo -e "\n${BLUE}========================================${NC}"