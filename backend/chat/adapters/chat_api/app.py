from classic.http_api import App

from backend.chat.application import services

from . import controllers


def create_app(
    chat: services.ChatService,
    user: services.UserService,
) -> App:

    app = App(prefix='/api')

    app.register(controllers.Chat(chat=chat))
    app.register(controllers.User(user=user))

    return app
