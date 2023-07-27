from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['complete']

class Role(models.Model):
    RoleID = models.AutoField(primary_key=True)
    RoleName = models.CharField(max_length=50)

    def __str__(self):
        return self.RoleName

class Users(models.Model):
    UserID = models.AutoField(primary_key=True)
    RoleID = models.ForeignKey('Role', on_delete=models.CASCADE)
    UserName = models.CharField(max_length=100)
    PasswordHash = models.CharField(max_length=128)
    FullName = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    PhoneNumber = models.CharField(max_length=20)

    def __str__(self):
        return self.UserName

class Vehicle(models.Model):
    VehicleID = models.AutoField(primary_key=True)
    RegistrationNumber = models.CharField(max_length=20)
    Make = models.CharField(max_length=100)
    Model = models.CharField(max_length=100)
    Capacity = models.FloatField()

    def __str__(self):
        return self.RegistrationNumber

class DeliveryStatus(models.Model):
    StatusID = models.AutoField(primary_key=True)
    EstimatedArrivalTime = models.DateTimeField()
    ActualArrivalTime = models.DateTimeField()
    DepartedTime = models.DateTimeField()
    Status = models.CharField(max_length=50)

    def __str__(self):
        return self.Status

class Address(models.Model):
    AddressID = models.AutoField(primary_key=True)
    Street = models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Province = models.CharField(max_length=100)
    ZIPCode = models.CharField(max_length=20)
    Country = models.CharField(max_length=100)

    def __str__(self):
        return f"Address {self.AddressID}"

class Customer(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    AddressID = models.ForeignKey('Address', on_delete=models.CASCADE)
    Name = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField(max_length=100)

    def __str__(self):
        return self.Name

class Order(models.Model):
    OrderID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey('Customer', on_delete=models.CASCADE)
    OrderDate = models.DateTimeField()
    OrderConfirmation = models.CharField(max_length=50)
    OrderPrice = models.DecimalField(max_digits=10, decimal_places=2)
    Category = models.CharField(max_length=50)

    def __str__(self):
        return f"Order {self.OrderID}"

class Payment(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey('Order', on_delete=models.CASCADE)
    PaymentStatus = models.CharField(max_length=50)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentDate = models.DateTimeField()
    PaymentMethod = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment {self.PaymentID}"

class Route(models.Model):
    RouteID = models.AutoField(primary_key=True)
    Origin = models.CharField(max_length=100)
    Destination = models.CharField(max_length=100)
    Distance = models.FloatField()

    def __str__(self):
        return f"Route {self.RouteID}"
    
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

class Assignment(models.Model):
    AssignmentID = models.AutoField(primary_key=True)
    DriverID = models.ForeignKey('Driver', on_delete=models.CASCADE)
    VehicleID = models.ForeignKey('Vehicle', on_delete=models.CASCADE)

    def __str__(self):
        return f"Assignment {self.AssignmentID}"

class Shipment(models.Model):
    ShipmentID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey('Order', on_delete=models.CASCADE)
    RouteID = models.ForeignKey('Route', on_delete=models.CASCADE)
    StatusID = models.ForeignKey('DeliveryStatus', on_delete=models.CASCADE)
    CustomerID = models.ForeignKey('Customer', on_delete=models.CASCADE)
    AssignmentID = models.ForeignKey('Assignment', on_delete=models.CASCADE)

    def __str__(self):
        return f"Shipment {self.ShipmentID}"


