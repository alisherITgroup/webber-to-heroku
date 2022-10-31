from webber.router import Path
from views import home

routes = [
    Path("/", home),
]    
