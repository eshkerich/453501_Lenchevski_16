from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication
from .models import Item
from .serializers import ItemSerializer
from .csrf_exempt import CsrfExemptSessionAuthentication

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [CsrfExemptSessionAuthentication]  # Отключаем CSRF для API
    
    def get_permissions(self):
        """
        Настройка прав в зависимости от действия
        """
        if self.action in ['list', 'retrieve']:
            # Просмотр списка и деталей доступен всем
            permission_classes = [permissions.AllowAny]
        else:
            # Создание, изменение и удаление только для авторизованных
            permission_classes = [permissions.IsAuthenticated]
        
        return [permission() for permission in permission_classes]
    
    def perform_create(self, serializer):
        serializer.save()