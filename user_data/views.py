from django.shortcuts import render_to_response 
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from user_data.models import User_data
from qlinarny.constant import *


def index(request, user_name):	
	return render_to_response('index.html', RequestContext(request,{'login': '' ,'content': main_content(request)}))
