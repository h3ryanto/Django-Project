from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

# Create your views here.

def index(request):
    context = {
        'link':"logout", 
        'inventory':'inventory',   
    }
    if not request.user.is_authenticated:
       return redirect('login_user')

    return render(request, 'index.html', context)

def login_user(request):
    contect = {
        'page_title': 'Please sign in'
    }
    user = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('inventory/')
   
        else:
            return redirect('login_user')
    else:
        # return redirect('index')
        return render(request, 'login.html', contect)


@login_required(login_url='/accounts/login/')
def logoutView(request):
	context = {
		'page_title':'logout'
	}

	if request.method == "POST":
		# if request.POST['logout'] == 'Submit':
		logout(request)

		return redirect('index')
        	


	return render(request, 'logout.html', context)