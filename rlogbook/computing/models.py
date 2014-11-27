from django.db import models


class OperatingSystem(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Computer(models.Model):
    description = models.CharField(max_length=200, blank=True)
    hostname = models.CharField(max_length=200, blank=True)
    os = models.ForeignKey(OperatingSystem, blank=True)
    room = models.ForeignKey('facility.room')

    def __unicode__(self):
        return self.hostname
