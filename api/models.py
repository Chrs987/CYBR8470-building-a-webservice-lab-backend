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

class Breed(models.Model):
    name = models.CharField(max_length=20)
    SIZE_CHOICE = (('tiny', 'Tiny'),
                    ('small', 'Small'),
                    ('medium', 'Medium'),
                    ('large', 'Large'))
    size = models.CharField(max_length=20, choices = SIZE_CHOICE)
    NUM_CHOICE = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
        (5,5)
    )

    friendliness = models.IntegerField(choices = NUM_CHOICE)
    trainability = models.IntegerField(choices = NUM_CHOICE)
    sheddingamount = models.IntegerField(choices = NUM_CHOICE)
    exerciseneeds = models.IntegerField(choices = NUM_CHOICE)

    def __str__(self):
        return str(self.name)

class BreedAdmin(admin.ModelAdmin):
    list_display = ('name', 'size')

class Dog(models.Model):
    name = models.CharField(max_length = 30)
    age = models.IntegerField()
    breed = models.ForeignKey(Breed, on_delete = models.CASCADE)
    gender = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    favourite_food = models.CharField(max_length=20)
    favourite_toy = models.CharField(max_length = 30)

class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'age')
