from django.db import models

class DeliveryStatus(models.Model):
    StatusID = models.AutoField(primary_key=True)
    EstimatedArrivalTime = models.DateTimeField()
    ActualArrivalTime = models.DateTimeField()
    DepartedTime = models.DateTimeField()
    Status = models.CharField(max_length=50)

    def __str__(self):
        return self.Status
