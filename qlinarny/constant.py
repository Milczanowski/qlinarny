from django.template.loader import get_template
from django.template import RequestContext

def login(request, message):
	return get_template('login.html').render(RequestContext(request,{'message': message}))

def main_content(request):
	return get_template('content.html').render(RequestContext(request,{}))

def register(request, message):		
	return get_template('rejestracja.html').render(RequestContext(request,{'message': message}))



	