from django.urls import path
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from django.middleware.csrf import get_token
import json

@ensure_csrf_cookie
def get_csrf_token(request):
    return JsonResponse({'csrfToken': get_token(request)})

@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                response = JsonResponse({
                    'success': True,
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                    }
                })
                return response
            else:
                return JsonResponse({
                    'success': False,
                    'error': 'Неверное имя пользователя или пароль'
                }, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return JsonResponse({'success': True})
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def user_view(request):
    if request.user.is_authenticated:
        return JsonResponse({
            'id': request.user.id,
            'username': request.user.username,
            'email': request.user.email,
        })
    return JsonResponse({'detail': 'Not authenticated'}, status=401)

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user/', user_view, name='user'),
    path('csrf/', get_csrf_token, name='csrf'),
]