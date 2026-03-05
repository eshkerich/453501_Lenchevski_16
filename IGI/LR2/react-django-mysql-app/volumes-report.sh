#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo -e "${GREEN}ОТЧЕТ ПО ТОМАМ DOCKER${NC}"
echo -e "${BLUE}========================================${NC}"

# Список всех томов
echo -e "\n${YELLOW}Список томов:${NC}"
docker volume ls | grep 16

# Информация о каждом томе
for volume in $(docker volume ls -q | grep 16); do
    echo -e "\n${GREEN}Том: $volume${NC}"
    docker volume inspect $volume | grep -E '"Mountpoint"|"Labels"' -A 2 | head -5
    
    # Показываем размер тома (если возможно)
    MOUNTPOINT=$(docker volume inspect $volume --format '{{.Mountpoint}}')
    if [ -d "$MOUNTPOINT" ]; then
        SIZE=$(sudo du -sh $MOUNTPOINT 2>/dev/null | cut -f1)
        echo -e "Размер: ${YELLOW}${SIZE:-0}${NC}"
    fi
done

echo -e "\n${BLUE}========================================${NC}"