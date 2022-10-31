

class Path:
    def __init__(self, path, func):
        self.path = path
        self.func = func
    def match(self, path):
        if self.path == path:
            return True
        return False

class Router:
    def __init__(self, routes=None):
        self.routes = list(routes) if routes else []
    def add_route(self, path):
        self.routes.append(path)
    def get_route(self, path):
        for route in self.routes:
            if route.match(path):
                return route.func
        return None
        

    