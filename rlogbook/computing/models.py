from django.db import models


class OperatingSystem(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class IPPolicy(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Sector(models.Model):
    name = models.CharField(max_length=200)
    from_ip = models.GenericIPAddressField()
    to_ip = models.GenericIPAddressField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class Subnet(models.Model):
    name = models.CharField(max_length=200)
    from_ip = models.GenericIPAddressField()
    to_ip = models.GenericIPAddressField()
    sector = models.ForeignKey(Sector, null=True)

    def __unicode__(self):
        return u"[{0}] {1}".format(self.sector, self.name)

    class Meta:
        ordering = ('sector', 'name')


class ComputerType(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', )


class CommonComputerInfo(models.Model):
    pass

    class Meta:
        abstract = True


class Warranty(models.Model):
    name  = models.CharField(max_length=200)
    warranty_length = models.PositiveSmallIntegerField(null=True, blank=True)

    def __unicode__(self):
        if self.warranty_length:
            return "{0} ({1} months)".format(self.name, self.warranty_length)
        return self.name

    class Meta:
        ordering = ('name', )


class RRZELicense(models.Model):
    name = models.CharField(max_length=200)
    order_nr = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name', 'order_nr')


class Printer(models.Model):
    manufacturer = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    PRINTER_TYPE_CHOICES = (
        ('0', 'laser'),
        ('1', 'ink-jet'),
        ('2', 'dot-matrix'),
        ('3', 'lcd/led'),
        ('4', 'thermal'),
    )
    printer_type = models.CharField(max_length=1, choices=PRINTER_TYPE_CHOICES)
    color = models.BooleanField(default=True)

    name = models.CharField(max_length=200, null=True, blank=True)

    inventory_number = models.CharField(max_length=200, null=True, blank=True)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    mac_address = models.CharField(max_length=17, null=True, blank=True)
    subnet = models.ForeignKey(Subnet, null=True, blank=True)
    dns_cname = models.CharField(max_length=200, null=True, blank=True)
    dns_hinfo_computer = models.CharField(max_length=200, null=True, blank=True)
    ip_policy = models.ForeignKey(IPPolicy, null=True, blank=True)

    hostname = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey('facility.user', null=True, blank=True)
    room = models.ForeignKey('facility.room', null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    prior_purpose = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)

    repair_log = models.TextField(null=True, blank=True)

    # Warranty and purchase information
    warranty = models.ForeignKey(Warranty, null=True, blank=True)
    purchase_date = models.DateField('purchase date', null=True, blank=True)

    def __unicode__(self):
        return self.name or self.hostname or 'Printer'



class Computer(models.Model):
    inventory_number = models.CharField(max_length=200, null=True, blank=True)
    serial_number = models.CharField(max_length=200, null=True, blank=True)
    mac_address = models.CharField(max_length=17, null=True, blank=True)
    subnet = models.ForeignKey(Subnet, null=True, blank=True)
    dns_cname = models.CharField(max_length=200, null=True, blank=True)
    dns_hinfo_computer = models.CharField(max_length=200, null=True, blank=True)
    ip_policy = models.ForeignKey(IPPolicy, null=True, blank=True)
    os = models.ForeignKey(OperatingSystem, null=True, blank=True)
    expiration_date = models.DateTimeField('expiration date', null=True, blank=True)
    software_licenses = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    computer_type = models.ForeignKey(ComputerType, null=True, blank=True)
    hostname = models.CharField(max_length=200, null=True, blank=True)
    user = models.ForeignKey('facility.user', null=True, blank=True)
    room = models.ForeignKey('facility.room', null=True, blank=True)
    purpose = models.TextField(null=True, blank=True)
    prior_purpose = models.TextField(null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)

    repair_log = models.TextField(null=True, blank=True)

    # Hardware
    ram = models.PositiveSmallIntegerField(null=True, blank=True)

    # Software
    standard_software = models.CharField(max_length=200, null=True, blank=True)
    additional_software = models.CharField(max_length=200, null=True, blank=True)
    rrze_licenses = models.ManyToManyField(RRZELicense, blank=True)

    # Warranty and purchase information
    warranty = models.ForeignKey(Warranty, null=True, blank=True)
    purchase_date = models.DateField('purchase date', null=True, blank=True)

    # Apple specific
    mac_airport = models.CharField(max_length=17, null=True, blank=True)
    mac_bluetooth = models.CharField(max_length=17, null=True, blank=True)
    model_year = models.CharField(max_length=50, null=True, blank=True)
    part_no = models.CharField(max_length=50, null=True, blank=True)
    netrestore_image = models.CharField(max_length=200, null=True, blank=True)

    #todo = models.TextField()

    def __unicode__(self):
        return self.name or self.hostname or 'Computer'


