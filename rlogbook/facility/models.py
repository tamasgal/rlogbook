from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name


class Room(models.Model):
    building = models.ForeignKey(Building)
    room_number = models.CharField(max_length=10)

    def __unicode__(self):
        return "{0} {1}".format(self.building.acronym, self.room_number)


class Location(models.Model):
    room = models.ForeignKey(Room)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return "{0} - {1}".format(self.room, self.description)


class User(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
