from backend.chat.adapters.storage import storage

import jwt


def is_authenticated(func):
    def wrapper(self, request, response):
        method, token = request.get_header('Authorization').split()
        if method in ('Bearer', 'JWT'):
            data = jwt.decode(token, storage.SECRET, algorithms=["HS256"])
            if data['user_id'] in storage.users:
                request.context = data
                func(self, request, response)
            else:
                raise ValueError
    return wrapper

