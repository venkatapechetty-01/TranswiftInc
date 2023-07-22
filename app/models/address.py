from django.db import models

class Address(models.Model):
    AddressID = models.AutoField(primary_key=True)
    Street = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Province = models.CharField(max_length=100)
    ZIPCode = models.CharField(max_length=20)
    Country = models.CharField(max_length=100)

    def __str__(self):
        return f"Address {self.AddressID}"
