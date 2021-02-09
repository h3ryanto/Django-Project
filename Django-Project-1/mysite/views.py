from django.shortcuts import render
from .form import login

def index(request):
    form_login = login()
    context ={
            'form': form_login,
    }
    
  
    if request.method == 'POST': 
	    print(request.POST)

    return render(request,'index.html', context)


