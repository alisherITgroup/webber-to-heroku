
from webber.request import Request
import json

class Response:
    def __init__(self, request: Request, status_code: str, content_type: str):
        self.status_code: str = status_code
        self.start_response: Callable = request.start_response
        self.content_type: str = content_type
        self.headers: list = [("Content-Type", self.content_type)]
        self.response_content = []
    def make_response(self):
        self.start_response(self.status_code, self.headers)
        return self.response_content

class HttpResponse(Response):
    def __init__(self, request: Request, content, status_code: str='200 OK', content_type: str="text/html"):
        super().__init__(request, status_code, content_type)
        if type(content) == str:
            content = content.encode()
        self.response_content.append(content)

class JsonResponse(Response):
    def __init__(self, request: Request, content, status_code: str='200 OK', content_type: str="application/json"):
        super().__init__(request, status_code, content_type)
        content = json.dumps(content).encode()
        self.response_content.append(content)
        
        
class ErrorResponse(Response):
    def __init__(self, request: Response, error_code: str):
        super().__init__(request, "404 topilmadi", "text/html")
        
        
class Http404(ErrorResponse):
    def __init__(self, request):   
        super().__init__(request, "404 topilmadi")
        self.response_content.append("404 topilmadi".encode())   
  
    