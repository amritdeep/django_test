# Create your views here.

from django.http import HttpResponse

def hello(request):
	name = "amrit"
	html = "<html><body>It me %s.</body></html>" % name
    return HttpResponse(html)