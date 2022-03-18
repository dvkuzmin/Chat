from classic.components import component
from backend.chat.application import services
from falcon import Request, Response
import falcon
import json


# @component
class ChatInfo:
    chat = services.ChatService()

    def on_get(self, req: Request, resp: Response, chat_id: str):
        """Просмотр инфо о чате, Get запрос вида /chats/{chat_id}/"""
        chat = self.chat.get_chat_by_id(int(chat_id))
        if chat:
            resp.body = json.dumps({'title': chat.title})
        else:
            raise falcon.HTTP_404

    def on_post(self, req: Request, resp: Response):
        """Изменение инфо о чате, Post запрос вида
        {
        "id": int,
        "title": str
        }
        """
        data = req.get_media()
        chat_id = int(data['id'])
        title = data['title']
        self.chat.modify_chat_info(chat_id, title)
        resp.body = json.dumps({'modified': f'{chat_id = } with {title = }'})
        resp.location = f'/chat/{chat_id}/'


class ChatCreate:
    chat = services.ChatService()

    def on_post(self, req: Request, resp: Response):
        """Создание чата, Post запрос вида
        {
        "title": str,
        "chat_owner": int
        }
        """
        data = req.get_media()
        chat_owner = int(data['chat owner'])
        title = data['title']
        new_chat = self.chat.create_chat(title, chat_owner)
        resp.body = json.dumps({f'created': f'new chat with title {new_chat.title} with id = {new_chat.id}'})
