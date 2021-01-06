from django.db import models

# Create your models here.
class Device(models.Model):
    brand = models.CharField(max_length=100, blank=False)
    model = models.CharField(max_length=100, blank=False)
    serial = models.IntegerField()
    price = models.IntegerField()

    choices = {
        ('SOLD', 'Item is Sold'),
        ('AVAILABLE', 'Item is ready to be purchased'),
        ('OUT OF STOCK', 'Item is out of stock'),
    }
    status = models.CharField(max_length=12, choices=choices, default="SOLD")

    class Meta:
        abstract = True

    def __str__(self):
        return '{0} {1} ({2})'.format(self.brand, self.model, self.status)

class Laptop(Device):
    pass

class Desktop(Device):
    pass

class Mobile(Device):
    pass
