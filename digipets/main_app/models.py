from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.

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
    species = models.CharField(max_length=10, choices=SPECIES)
    personality = models.CharField(max_length=20, choices=PERSONALITIES)
    # image = models.ImageField()
    birthday = models.DateField('Birthday')
    # joy, fatigue, sleep, level will be added later on. This so far should be enough
    # to get our CRUD going
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'Digipet_id': self.id})
