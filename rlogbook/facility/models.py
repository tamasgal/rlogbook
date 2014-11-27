from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=10)


class Room(models.Model):
    building = models.ForeignKey(Building)
    room_number = models.CharField(max_length=10)


class Location(models.Model):
    room = models.ForeignKey(Room)
    description = models.CharField(max_length=200)


class User(models.Model):
    name = models.CharField(max_length=200)
