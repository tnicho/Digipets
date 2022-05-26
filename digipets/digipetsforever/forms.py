from django.forms import ModelForm
from .models import Digipet

class DigipetsForm(ModelForm):
  class Meta:
    model = Digipet
    fields = ['name', 'species', 'birthday', 'personality']