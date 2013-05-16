from django.shortcuts import render_to_response 
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from user_data.models import User_data
from qlinarny.constant import *
from django.core.mail import send_mail
from constant.models import Constant
from przepis.forms import *



def dodaj(request):
	if request.methods = "POST":
		if request.user.is_authenticated():

		else:


	else
		return HttpResponseRedirect("/przepis/dodaj")
