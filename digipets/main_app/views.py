from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from .models import Digipet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DigipetsForm
from django.forms import ModelForm
from django.views.generic.edit import UpdateView
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

def digipets_feed (request, digipet_id):
  Digipet.objects.get(id=digipet_id).feed
  return redirect(request, 'digipets_detail', digipet_id = digipet_id)
  
class DigipetCreate(CreateView):
  model = Digipet
  fields = ['name', 'species', 'personality', 'birthday']
  # digipets_form = DigipetsForm()
  # success_url = '/digipets/'



  def form_valid(self, form):
    form.instance.user = self.request.user
    # taking the user and assigning them to the form instance
    return super().form_valid(form)

class DigipetUpdate(UpdateView):
  model = Digipet
  fields = ['name', 'personality']
