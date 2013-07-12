# Create your views here.

from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.views.generic.base import TemplateView

def hello(request):
	name = "amrit"
	html = "<html><body>It me %s.</body></html>" % name
	return HttpResponse(html)

def hello_template(request):
	name = "amrit"
	t = get_template('hello.html')
	html = t.render(Context({'name' : name}))
	return HttpResponse(html)

def hello_template_simple(request):
	name = "amrit"
	return render_to_response('hello.html', {'name' : name})


class HelloTemplate(TemplateView):

	template_name = 'hello_class.html'

	def get_context_date(self, **kwargs):
		context = super(HelloTemplate, self).get_context_date(**kwargs)
		context['name'] = 'amrit'
		return context
