from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.views.generic.edit import CreateView
from .models import Digipet
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DigipetsForm
from django.forms import ModelForm
# Create your views here.


def home(request):
  return render(request, 'home.html')

def landing(request):
  return render(request, 'landing.html')

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
  
class DigipetCreate(CreateView):
  model = Digipet
  fields = ['name', 'species', 'personality', 'birthday']
  # digipets_form = DigipetsForm()
  # success_url = '/digipets/'



  def form_valid(self, form):
    form.instance.user = self.request.user
    # taking the user and assigning them to the form instance
    return super().form_valid(form)