#from django.http import request
from django.shortcuts import render,redirect,HttpResponse
from .form import AddLinkForm
from .models import Link
from django.views.generic import DeleteView
from django.contrib.auth import authenticate, login, logout
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .users import CreateUserForm,UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import *


def home(request):
    not_discounted = 0
    error = None

    form = AddLinkForm(request.POST or None)
    if request.method == 'POST':
        try:
            if form.is_valid():
                form.save()
        except AttributeError:
                error = 'Earth to Huston ....we cant get the name or the price.'
        except:
                error = 'Chief.....we got some errors here.'

 
    form = AddLinkForm()

    qs = Link.objects.all()
    items = qs.count()

    if items >0:
        discounted_items =[]
        for item in qs:
            if item.old_price > item.current_price:
               discounted_items.append(item)
               not_discounted = len(discounted_items)

    context ={
        'qs':qs,
        'items':items,
        'not_discounted':not_discounted,
        'form':form,
        'error':error,
    }        
    return render(request,'links/kit.html',context)

class LinkDeleteView(DeleteView):
    model = Link
    template_name = 'links/cn_del.html'
    success_url = reverse_lazy('home')

def update_prices(request):
    qs = Link.objects.all()
    for link in qs:
        link.save()
    return redirect('home')

def login(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return render(request,'links/kit.html')
            else:
                    messages.info(request, 'Oops looks like the Username or Password is wrong')

    context = {}
    return render(request, 'links/login.html', context)

def register(request):

      users = CreateUserForm()
      if request.method == 'POST':
          users = CreateUserForm(request.POST)
          if users.is_valid():
              users.save()
              user = users.cleaned_data.get('username')
              messages.success(request, 'Account was created for ' + user)
              
              return redirect('login')
      context = {'users':users}
      return render(request, 'links/reg.html', context)

def index(request):
    return render(request,'links/index.html')

def UserLogout(request):
	logout(request)
	return redirect('login')
	