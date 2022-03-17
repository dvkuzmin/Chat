import falcon
from backend.chat.adapters.chat_api.controllers import ChatInfo, ChatCreate


app = falcon.App()

app.add_route('/chats/{chat_id}/', ChatInfo())
app.add_route('/chats/', ChatInfo())
app.add_route('/chat/create/', ChatCreate())


