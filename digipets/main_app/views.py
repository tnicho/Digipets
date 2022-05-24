from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView
from .models import Digipet
# Create your views here.


def home(request):
  return render(request, 'home.html')

def landing(request):
  return render(request, 'landing.html')

def digipets_detail(request, digipet_id):
  digipet = Digipet.objects.get(id=digipet_id)
  return render(request, 'digipets/detail.html', {'digipet': digipet})

def digipets_index(request):
  digipets = Digipet.objects.filter()
  return render(request, 'digipets/index.html', {'digipets': digipets})

def signup(request):
  error_message=''
  if request.method == "POST":
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class DigipetUpdate(UpdateView):
  model = Digipet
  fields = ['name', 'personality']