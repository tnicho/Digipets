from datetime import date
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django import forms
from datetime import datetime


# Create your models here.
# MOODS = (
#     ('Ha', 'Happy'),
#     ('Hu', 'Hungry'),
#     ('S', 'Smelly'),
#     ('B', 'Bored'),
#     ('R', 'Restless')
# )

SPECIES = (
    ('H', 'Huskey'),
    ('C', 'Corgi'),
    ('O', 'Otter')
)

PERSONALITIES = (
    ('T', 'Timid'),
    ('B', 'Brave'),
    ('N', 'Naughty'),
    ('C', 'Calm'),
    ('J', 'Jolly'),
    ('Q', 'Quirky'),
    ('S', 'Sassy')
)

class Digipet(models.Model):
  name = models.CharField(max_length=50)
  species = models.CharField(max_length=10, choices=SPECIES, default=SPECIES[0][0])
  # personality=models.CharField(label='What personality does your pet have?', widget=models.Select(choices=PERSONALITIES))
  personality = models.CharField(max_length=20, choices=PERSONALITIES, default=PERSONALITIES[0][0])
  #image = models.ImageField( default = "/static/digipets/assets/animals/corgi/1.svg")
  image = models.CharField(max_length=250, default = "/static/digipets/assets/animals/corgi/1.svg")
  birthday = models.DateField('Birthday')
  mood = models.CharField(max_length=20, default = 'hungry')
  #last_feed = models.DateField(default = datetime.now())

  #last_wash = models.DateField(default = datetime.now())
  #last_play = models.DateField(default = datetime.now())
  #last_walk = models.DateField(default = datetime.now())
  # mood = models.CharField(max_length = 20, choices=MOODS, default=MOODS[0][0])

  # joy, fatigue, sleep, level will be added later on. This so far should be enough
  # to get our CRUD going
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f'{self.name} {self.get_personality_display()}'

  def get_absolute_url(self):
    return reverse('detail', kwargs={'digipet_id': self.id})

  def feed (self):
    self.last_feed = self.get_time()

  def get_time(self):
	  return datetime.datetime.now()

