from django.db import models

class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    AddressID = models.ForeignKey('Address', on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField(max_length=100)

    def __str__(self):
        return self.Name
