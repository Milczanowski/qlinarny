from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.template import RequestContext
from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect, HttpResponse
from django.conf import settings
from qlinarny.constant import *
from django.core.mail import send_mail

def index(request):
	return render_to_response('index.html', RequestContext(request,{'login': login(request, '') ,'content': main_content(request)}))

def main_page(request):
	return HttpResponseRedirect("/")

def name(request, user_name):
	return HttpResponse(user_name) 

def profile(request):
	return HttpResponseRedirect("/%s" %request.user.username)
