import falcon
from backend.chat.adapters.chat_api.controllers import ChatInfo, ChatCreate
from wsgiref.simple_server import make_server

app = falcon.App()

app.add_route('/chatinfo/{chat_id}/', ChatInfo())
app.add_route('/chatinfo/', ChatInfo())
app.add_route('/chat/create/', ChatCreate())


with make_server('localhost', 8000, app) as httpd:
    print(f'Server running on http://localhost:{httpd.server_port} ...')
    httpd.serve_forever()