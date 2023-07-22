from django.db import models

class Driver(models.Model):
    DriverID = models.AutoField(primary_key=True)
    RoleID = models.ForeignKey('Role', on_delete=models.CASCADE)
    AddressID = models.ForeignKey('Address', on_delete=models.CASCADE)
    DriverName = models.CharField(max_length=100)
    MobileNumber = models.CharField(max_length=20)
    LicenseNumber = models.CharField(max_length=50)
    Salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.DriverName
