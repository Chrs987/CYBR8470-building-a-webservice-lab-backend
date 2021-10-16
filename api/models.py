from __future__ import unicode_literals

from django.db import models
from django.core.validators import *

from django.contrib.auth.models import User, Group

from django.contrib import admin
import base64

class Event(models.Model):
    eventtype = models.CharField(max_length=1000, blank=False)
    timestamp = models.DateTimeField()
    userid = models.CharField(max_length=1000, blank=True)
    requestor = models.GenericIPAddressField(blank=False)

    def __str__(self):
        return str(self.eventtype)

class EventAdmin(admin.ModelAdmin):
    list_display = ('eventtype', 'timestamp')

class ApiKey(models.Model):
    owner = models.CharField(max_length=1000, blank=False)
    key = models.CharField(max_length=5000, blank=False)

    def __str__(self):
        return str(self.owner) + str(self.key)

class ApiKeyAdmin(admin.ModelAdmin):
    list_display = ('owner','key')

#Stuff for new Lab
class Breed(models.Model):
    breed_size = [
        ('tiny', 'Tiny'),
        ('small', 'Small'),
        ('medium', 'Medium'),
        ('large', 'Large'),
        ]
    name = models.CharField(max_length=20)
    size = models.CharField(max_length=10, choices=breed_size, default='tiny')
    friendliness = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    trainability = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    sheddingAmount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    exerciseNeeds= models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

class Dog(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    gender = models.CharField(max_length=7)
    color = models.CharField(max_length=10)
    favoriteFood = models.CharField(max_length=10)
    favoriteToy = models.CharField(max_length=20)
