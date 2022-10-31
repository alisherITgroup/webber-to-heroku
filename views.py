from webber.response import HttpResponse
from webber.views import TemplateView

def home(request):
    template_file = TemplateView("index.html")
    template = template_file.to_html() 
    return HttpResponse(request, template)
