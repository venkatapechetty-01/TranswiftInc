from django.db import models

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey('Customer', on_delete=models.CASCADE)
    OrderDate = models.DateTimeField()
    OrderConfirmation = models.CharField(max_length=50)
    OrderPrice = models.DecimalField(max_digits=10, decimal_places=2)
    Category = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.OrderID}"
