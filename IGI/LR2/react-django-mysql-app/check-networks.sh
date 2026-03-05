#!/bin/bash

GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${YELLOW}=== Информация о сетях ===${NC}"
docker network ls | grep 16

echo -e "\n${YELLOW}=== Детальная информация о сетях ===${NC}"
for network in $(docker network ls --filter "name=16" -q); do
  network_name=$(docker network inspect $network --format '{{.Name}}')
  echo -e "\n${BLUE}Сеть: $network_name${NC}"
  docker network inspect $network | grep -E "Subnet|Gateway|Name.*_16" | head -10
  echo -e "${GREEN}Подключенные контейнеры:${NC}"
  docker network inspect $network --format='{{range $k, $v := .Containers}}{{$k}} {{$v.Name}} {{$v.IPv4Address}}{{"\n"}}{{end}}'
done

echo -e "\n${YELLOW}=== Информация о томах ===${NC}"
docker volume ls | grep 16

echo -e "\n${YELLOW}=== Размеры томов ===${NC}"
for volume in $(docker volume ls --filter "name=16" -q); do
  echo -n "$volume: "
  docker run --rm -v $volume:/data alpine du -sh /data 2>/dev/null || echo "empty"
done