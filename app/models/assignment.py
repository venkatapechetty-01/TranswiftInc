from django.db import models

class Assignment(models.Model):
    AssignmentID = models.AutoField(primary_key=True)
    DriverID = models.ForeignKey('Driver', on_delete=models.CASCADE)
    VehicleID = models.ForeignKey('Vehicle', on_delete=models.CASCADE)

    def __str__(self):
        return f"Assignment {self.AssignmentID}"
