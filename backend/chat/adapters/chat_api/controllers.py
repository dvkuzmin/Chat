from classic.components import component
from backend.chat.application import services
from falcon import Request, Response
import falcon
import json
from backend.chat.application.services import ChatInfoDTO


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
        try:
            chat_info = ChatInfoDTO(**req.get_media())
        except Exception:
            raise falcon.HTTP_400
        self.chat.modify_chat_info(chat_info)
        resp.body = json.dumps({'modified': f'{chat_info.id = } with {chat_info.title = }'})
        resp.location = f'/chat/{chat_info.id}/'


class ChatCreate:
    chat = services.ChatService()

    def on_post(self, req: Request, resp: Response):
        """Создание чата, Post запрос вида
        {
        "title": str,
        "chat_owner": int
        }
        """
        try:
            chat_info = ChatInfoDTO(**req.get_media())
        except Exception:
            raise falcon.HTTP_400
        new_chat = self.chat.create_chat(chat_info)
        resp.body = json.dumps({f'created': f'new chat with title {new_chat.title} with id = {new_chat.id}'})
