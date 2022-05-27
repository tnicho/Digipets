from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from .models import Digipet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DigipetsForm
from django.forms import ModelForm
from django.views.generic.edit import UpdateView, DeleteView
# Create your views here.


def home(request):
  return render(request, 'home.html')

def landing(request):
  return render(request, 'landing.html')

@login_required
def digipets_update(request, digipet_id):
  return render(request, 'digipets/update.html')

@login_required
def digipets_detail(request, digipet_id):
  digipet = Digipet.objects.get(id=digipet_id)
  return render(request, 'digipets/detail.html', {'digipet': digipet})

@login_required
def digipets_index(request):
  digipets = Digipet.objects.filter(user=request.user)
  # if Digipet.hungry == "happy":
  #   Digipet.hungry == "hungry"
  # else:
  #   Digipet.hungry == "happy"
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
  print("made it here")
  digipet = Digipet.objects.get(id=digipet_id)
  digipet.mood = 'Happy'
  digipet.save()
  return redirect('detail', digipet_id = digipet_id)
  
class DigipetCreate(LoginRequiredMixin, CreateView):
  model = Digipet
  #fields = ['name', 'species', 'personality', 'birthday', 'image']
  fields = ['name', 'personality', 'birthday', 'species', 'image']
  # digipets_form = DigipetsForm()
  #success_url = '/digipets/'

  def form_valid(self, form):
    form.instance.user = self.request.user
    # taking the user and assigning them to the form instance
    return super().form_valid(form)


class DigipetUpdate(LoginRequiredMixin, UpdateView):
  model = Digipet
  fields = ['name', 'personality']

class DigipetDelete(LoginRequiredMixin, DeleteView):
  model = Digipet
  success_url = '/digipets/'