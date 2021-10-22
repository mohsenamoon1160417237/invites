import jwt
import datetime
from rest_framework.response import Response


def login(user):

    payload = {
        "id" : user.id,
        "exp" : datetime.datetime.utcnow() + datetime.timedelta(hours=2),
        "iat" : datetime.datetime.utcnow()
    }

    token = jwt.encode(payload , 'secret' , algorithm='HS256')
    response = Response()
    response.set_cookie(key='jwt' , value=token , httponly=True)

    return [response , token]