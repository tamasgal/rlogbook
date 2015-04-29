from django.db import models


class Building(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=10)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', 'acronym')
        

class Room(models.Model):
    building = models.ForeignKey(Building)
    room_number = models.CharField(max_length=10)

    def __unicode__(self):
        return "{0} {1}".format(self.building.acronym, self.room_number)

    class Meta:
        ordering = ('building', 'room_number')


class Location(models.Model):
    room = models.ForeignKey(Room)
    description = models.CharField(max_length=200)

    def __unicode__(self):
        return "{0} - {1}".format(self.room, self.description)

    class Meta:
        ordering = ('room',)


class User(models.Model):
    name = models.CharField(max_length=200)
    arrival = models.DateField('arrival date', null=True, blank=True)
    departure = models.DateField('departure date', null=True, blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', 'arrival', 'departure')
