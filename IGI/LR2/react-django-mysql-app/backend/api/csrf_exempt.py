from rest_framework.authentication import SessionAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    SessionAuthentication без CSRF проверки для API
    """
    def enforce_csrf(self, request):
        return  # Не проверять CSRF