from django.db import models


class OperatingSystem(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name



class IPPolicy(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Subnet(models.Model):
    name = models.CharField(max_length=200)
    from_ip = models.CharField(max_length=15)
    to_ip = models.CharField(max_length=15)

    def __unicode__(self):
        return self.name


class Computer(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    hostname = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey('facility.user', null=True, blank=True)
    room = models.ForeignKey('facility.room', null=True, blank=True)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    ip = models.CharField(max_length=15, null=True, blank=True)
    mac_address = models.CharField(max_length=17, null=True, blank=True)
    subnet = models.ForeignKey(Subnet, null=True, blank=True)
    dns_cname = models.CharField(max_length=200, null=True, blank=True)
    dns_hinfo_computer = models.CharField(max_length=200, null=True, blank=True)
    ip_policy = models.ForeignKey(IPPolicy, null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    prior_purpose = models.TextField(null=True, blank=True)
    os = models.ForeignKey(OperatingSystem, null=True, blank=True)
    expiration_date = models.DateTimeField('expiration date', null=True, blank=True)
    software_licenses = models.CharField(max_length=200, null=True, blank=True)
    #todo = models.TextField()
    comment = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return self.name or self.hostname or 'Computer'


