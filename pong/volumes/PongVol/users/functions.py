
import jwt, datetime
from .models import User, TokensCustom




def gen_token(user):
    if user:
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=2),
            'iat': datetime.datetime.utcnow()
        }
        token  = jwt.encode(payload, 'secret', algorithm='HS256')
        decoded = jwt.decode(token,'secret', algorithms=['HS256'])
        savetoken = TokensCustom()
        savetoken.token = token
        savetoken.created_at = datetime.datetime.fromtimestamp(decoded['iat'])
        savetoken.expires_at = datetime.datetime.fromtimestamp(decoded['exp'])
        savetoken.user_id = user
        savetoken.save()
        return token