
import os
from webber.app import App
from webber.router import Path
from webber.response import HttpResponse
from wsgiref.simple_server import make_server


class AppRunner:
    def __init__(self, routes=[]):
        self.app = App()
        self.routes = routes
        self.app.set_routes(self.routes)
        self.server = make_server("127.0.0.1", 2000, self.app)

    def run(self):
        os.system("clear")
        print('[34m', "Welcome to Webber. Server is running on 127.0.0.1:2000")
        self.server.serve_forever()
    