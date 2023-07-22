from django.db import models

class Vehicle(models.Model):
    VehicleID = models.AutoField(primary_key=True)
    RegistrationNumber = models.CharField(max_length=20)
    Make = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Capacity = models.FloatField()

    def __str__(self):
        return self.RegistrationNumber
