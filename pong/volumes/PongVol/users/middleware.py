import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.deprecation import MiddlewareMixin
from django.contrib.auth.models import AnonymousUser
from .models import TokensCustom

User = get_user_model()
class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.user.is_anonymous:
            token = request.COOKIES.get('jwt')
            if token:
                try:
                    tok = TokensCustom.objects.filter(token = token).first()
                    if not tok or not tok.is_valid():
                        raise Exception
                    payload = jwt.decode(token, 'secret', algorithms=['HS256'])
                    user_id = payload.get('id')
                    user = User.objects.get(id=user_id)
                    request.user = user
                except (jwt.ExpiredSignatureError, jwt.InvalidTokenError, User.DoesNotExist):
                    request.user = AnonymousUser()
            else:
                request.user = AnonymousUser()
        
