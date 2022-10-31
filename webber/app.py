
from webber.request import Request
from webber.response import Http404
from webber.router import Router


class App:
    def __init__(self):
        self.router  = Router()

    def set_routes(self, routes: list):
        for path in routes:
            self.router.add_route(path)    
    

    def __call__(self, environ, start_response):
        request:Request = Request(environ, start_response)
        try:
            func = self.router.get_route(request.path)
            if func is not None:
                response: Response = func(request)
                return response.make_response()
            else:
                return Http404(request).make_response()
        except Exception as e: 
            print(e)
            return Http404(request).make_response()
      
    