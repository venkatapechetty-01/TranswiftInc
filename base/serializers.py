from rest_framework import serializers
from base.models import Vehicle, Driver, Address, Role

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vehicle 
        fields=('VehicleID','RegistrationNumber', 'Make', 'Model', 'Capacity')

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model=Driver 
        fields=('DriverID','RoleID','AddressID','DriverName','MobileNumber', 'LicenseNumber', 'Salary')
        
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model=Address 
        fields=('AddressID','Street','City','Province','ZIPCode', 'Country')
        
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Role 
        fields=('RoleID','RoleName')