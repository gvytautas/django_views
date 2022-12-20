from django.db import models


# Create your models here.

class VehicleModel(models.Model):
    brand = models.CharField(max_length=50, null=False, blank=False)
    model = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return f'{self.model}'


class Service(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f'{self.name} ({self.price})'


class Vehicle(models.Model):
    plate_number = models.CharField(max_length=50, null=False, blank=False)
    win_number = models.CharField(max_length=50, null=False, blank=False)
    client = models.CharField(max_length=50, null=False, blank=False)
    model = models.ForeignKey(VehicleModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.win_number


class Order(models.Model):
    date = models.DateField(null=False, blank=False)
    total_price = models.FloatField(null=False, blank=False)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.vehicle.win_number} ({self.total_price})'


class OrderDetail(models.Model):
    quantity = models.IntegerField(null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.order.vehicle.model.brand}'
