from django.db import models

class Shipment(models.Model):
    ShipmentID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey('Order', on_delete=models.CASCADE)
    RouteID = models.ForeignKey('Route', on_delete=models.CASCADE)
    StatusID = models.ForeignKey('DeliveryStatus', on_delete=models.CASCADE)
    CustomerID = models.ForeignKey('Customer', on_delete=models.CASCADE)
    AssignmentID = models.ForeignKey('Assignment', on_delete=models.CASCADE)

    def __str__(self):
        return f"Shipment {self.ShipmentID}"
