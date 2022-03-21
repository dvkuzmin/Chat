from backend.chat.application import services, interfaces
from .auth import is_authenticated

import falcon
from classic.components import component


@component()
class User:
    user: services.UserService

    def on_post_register(self, request, response):
        """Регистрация пользователя, POST запрос вида
        {
            "user_name": str,
            "password": str,
            "phone": str
        }
        """
        user = self.user.create_user(**request.media)
        response.media = {
            'message': f'User with id {user.id = } registration complete'
        }

    def on_post_login(self, request, response):
        """Авторизация пользователя, POST запрос вида
        {
            "user_name": str,
            "password": str
        }
        """
        token = self.user.login(**request.media)
        if token:
            response.set_header("AUTH-TOKEN", token)
            response.media = {
                'message': 'Login complete successful'
            }
        else:
            response.media = {
                'invalid': 'no user'
            }

@component
class Chat:
    chat: services.ChatService

    @is_authenticated
    def on_get_info(self, request, response):
        """Просмотр инфо о чате, Get запрос вида /api/chat/info?chat_id=1"""
        chat = self.chat.get_chat_info(**request.params, **request.context)
        response.media = {f'chat info': chat.title}
        response.status = falcon.HTTP_200


    @is_authenticated
    def on_post_update_info(self, request, response):
        """Изменение инфо о чате, Post запрос вида
           {
            "chat_id": int,
            "title": str
            }
            """
        chat = self.chat.update_chat_info(**request.media, **request.context)
        response.media = {f'chat with {chat.id = }': f'title was modified {chat.title = }'}

    @is_authenticated
    def on_get_users(self, request, response):
        """Просмотр всех пользователей чата, GET запрос вида /api/chat/users?chat_id=1"""
        users = self.chat.get_all_users(**request.params, **request.context)
        response.media = {'chat users': users}
        response.status = falcon.HTTP_200

    @is_authenticated
    def on_get_messages(self, request, response):
        """Просмотр всех сообщений чата, GET запрос вида /api/chat/messages?chat_id=1"""
        messages = self.chat.get_all_messages(**request.params, **request.context)
        response.media = {'chat messages': messages}
        response.status = falcon.HTTP_200

    @is_authenticated
    def on_post_create(self, request, response):
        """Создание чата, Post запрос вида
        {
        "title": str,
        "chat_owner": int
        }
        """
        new_chat = self.chat.create_chat(**request.media, **request.context)
        response.media = {'created': f'new chat with title {new_chat.title} with id = {new_chat.id}'}
        response.status = falcon.HTTP_200

    @is_authenticated
    def on_post_message(self, request, response):
        """Отправка сообщения в чат, POST запрос вида
        {
         "chat_id": int,
         "message": str
         }
         """
        new_message = self.chat.send_message(**request.media, **request.context)
        response.media = {"message created": new_message.message}

    @is_authenticated
    def on_get_remove(self, request, response):
        """Удаление чата, GET запрос вида /api/chat/remove?chat_id=1"""
        self.chat.remove_chat(**request.params, **request.context)
        response.media = 'chat was removed'

    @is_authenticated
    def on_post_invite_user(self, request, response):
        """Отправка сообщения в чат, POST запрос вида
        {
         "chat_id": int,
         "guest_id": int
         }
         """
        self.chat.invite_user(**request.media, **request.context)
        response.media = "user added to chat"
