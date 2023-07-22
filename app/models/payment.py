from django.db import models

class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey('Order', on_delete=models.CASCADE)
    PaymentStatus = models.CharField(max_length=50)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentDate = models.DateTimeField()
    PaymentMethod = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.PaymentID}"
