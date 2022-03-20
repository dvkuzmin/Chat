from backend.chat.adapters import storage, chat_api
from backend.chat.application import services


class Application:

    chat = services.ChatService(
        chat_repo=storage.repositories.ChatRepo(),
        user_repo=storage.repositories.UserRepo(),
        message_repo=storage.repositories.MessageRepo(),
    )
    user = services.UserService(
        user_repo=storage.repositories.UserRepo(),
    )


app = chat_api.create_app(
    chat=Application.chat,
    user=Application.user,
)
