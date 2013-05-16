from django.shortcuts import render_to_response 
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from user_data.models import User_data
from qlinarny.constant import *
from django.core.mail import send_mail
from constant.models import Constant
import random


def wyloguj(request):
    logout(request)
    return HttpResponseRedirect("/")

def profile(request):
    return HttpResponseRedirect("/")

def stworzone(request):
    return render_to_response('message.html', RequestContext(request,{'message':'dziekujemy za rejestracje kliknij link email'}))


def index(request):
    if request.method == 'POST':
        form = FormularzLogowania(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            login(request,user)
            template = get_template("index.html")
            variables = RequestContext(request,{'user':user})
            output = template.render(variables)
            return HttpResponseRedirect("/")                         
    else: 
        form = FormularzLogowania()
    template = get_template("registration/login.html")    
    variables = RequestContext(request,{'form':form})
    output = template.render(variables)
    return HttpResponse(output)


def zarejestruj(request):
    if request.method == "POST":
        pass1 = request.POST['password']
        pass2 = request.POST['password2']
        if(pass1 == pass2):
            if(len(pass1)>=8):
                username = request.POST['username']
                try:
                    anyuser = User.objects.get(username= username)
                    return render_to_response('index.html', RequestContext(request,{'message':'podana nazwa urzytkownika już istnieję'}))
                except Exception, e:
                    email = request.POST['email']
                    try:
                        anyuser = User.objects.get(email = email)
                        return render_to_response('index.html', RequestContext(request,{'message':'istnieje już konto z podanym adresem email'}))
                    except Exception, e:                   
                        if(find(email)):
                            user = User.objects.create_user(username, email, pass1)    
                            user.is_active = False                       
                            user.save()
                            r = random.randint(0,999999)
                            u = User_data(random_activate_code = r, user = user)
                            u.save()
                            message = Constant.objects.get(id= 1).register_email_message
                            message = message.replace("{{link}}","http://127.0.0.1:8000/accounts/%s/%s/aktywuj" %(username, r))
                            send_mail('Qlinarny.pl aktywacja', message, 'from@example.com', [email], fail_silently=False)                        
                            return HttpResponseRedirect("/accounts/created")
                        else:
                            return render_to_response('index.html', RequestContext(request,{'message': 'Niepoprawny email'}))                                   
            else:
             return render_to_response('register.html', RequestContext(request,{ 'message': "hasło 8 znaków"}))  
        else:
            return render_to_response('register.html', RequestContext(request,{'message': 'Hasła powinny być takie same '}))
    else:
        return render_to_response('register.html', RequestContext(request,{}))




def aktywuj(request, user_name, user_id):
    if(User.objects.get(username= user_name).user_data.random_activate_code == int(user_id)):
        u =User.objects.get(username = user_name)
        u.is_active = True
        u.save()        
        return render_to_response('message.html', RequestContext(request,{'message': "dziekujemy za aktywacje możesz już sie zalogować"}))
    else:
        return HttpResponseRedirect("/")

def find(email):
    for word in email:
        if word == '@':
            return True
    return False






