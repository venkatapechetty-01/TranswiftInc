from django.db import models

class Route(models.Model):
    RouteID = models.AutoField(primary_key=True)
    Origin = models.CharField(max_length=100)
    Destination = models.CharField(max_length=100)
    Distance = models.FloatField()

    def __str__(self):
        return f"Route {self.RouteID}"
