#!/bin/bash

# Цвета для вывода
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m'

# Загрузка переменных из .env файла
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo -e "${RED}Файл .env не найден!${NC}"
    exit 1
fi

echo -e "${YELLOW}=== Управление бэкапами MySQL ===${NC}"

case "$1" in
  create)
    echo -e "${GREEN}Создание бэкапа...${NC}"
    
    # Создание директории для бэкапов если её нет
    mkdir -p ./backups
    
    # Имя файла с датой
    BACKUP_FILE="./backups/backup_$(date +%Y%m%d_%H%M%S).sql"
    
    # Создание бэкапа с передачей пароля
    docker exec mysql_db_16 mysqldump -u root -p${MYSQL_ROOT_PASSWORD} --all-databases > ${BACKUP_FILE}
    
    # Проверка размера файла
    if [ -s ${BACKUP_FILE} ]; then
        echo -e "${GREEN}✓ Бэкап создан: ${BACKUP_FILE}${NC}"
        echo -e "  Размер: $(du -h ${BACKUP_FILE} | cut -f1)"
    else
        echo -e "${RED}✗ Бэкап пустой! Ошибка подключения к MySQL${NC}"
        rm -f ${BACKUP_FILE}
    fi
    ;;
    
  list)
    echo -e "${GREEN}Список бэкапов:${NC}"
    if [ -d "./backups" ] && [ "$(ls -A ./backups)" ]; then
        ls -lh ./backups/*.sql 2>/dev/null || echo "  Нет .sql файлов"
    else
        echo "  Нет бэкапов"
    fi
    ;;
    
  restore)
    if [ -z "$2" ]; then
        echo -e "${RED}Укажите файл для восстановления${NC}"
        echo "Использование: $0 restore <файл>"
        exit 1
    fi
    
    if [ ! -f "$2" ]; then
        echo -e "${RED}Файл $2 не найден${NC}"
        exit 1
    fi
    
    echo -e "${YELLOW}Восстановление из $2...${NC}"
    cat "$2" | docker exec -i mysql_db_16 mysql -u root -p${MYSQL_ROOT_PASSWORD}
    
    if [ $? -eq 0 ]; then
        echo -e "${GREEN}✓ Восстановление завершено успешно${NC}"
    else
        echo -e "${RED}✗ Ошибка при восстановлении${NC}"
    fi
    ;;
    
  *)
    echo "Использование: $0 {create|list|restore <файл>}"
    ;;
esac