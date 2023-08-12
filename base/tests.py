from django.test import TestCase, Client
from django.urls import reverse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Vehicle, Driver, Role, Address
from .serializers import VehicleSerializer
from .views import vehicleApi
import json

class TranswiftApiTest(TestCase):
    def test_get_vehicles(self):
        # Create some test vehicles
        Vehicle.objects.create(VehicleID=1, RegistrationNumber='CMDJ123', Model='Sedan', Capacity=4)
        Vehicle.objects.create(VehicleID=2, RegistrationNumber='ONT123', Model='SUV', Capacity=4)

        # Send a GET request
        response = self.client.get(reverse('base:addVehicle'))

        # Verify the response
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'CMDJ123')
        self.assertContains(response, 'ONT123')

    def test_post_vehicle(self):
        vehicle_data = {
            'VehicleID': 5,
            'RegistrationNumber': 'TEST180',
            'Make':'2018',
            'Model': 'Sedan',
            'Capacity': 4
        }


        response = self.client.post(reverse('base:vehicles'), data=vehicle_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Added Successfully')

        # Verify that the vehicle was actually added to the database
        self.assertEqual(Vehicle.objects.count(), 1)
        self.assertEqual(Vehicle.objects.get().RegistrationNumber, 'TEST180')

    '''def test_update_vehicle(self):
        # Create a vehicle to update
        vehicle = Vehicle.objects.create(VehicleID=1, RegistrationNumber='CMDJ123', Model='SUV', Capacity=4)

        updated_vehicle_data = {
            'VehicleID': 1,
            'RegistrationNumber': 'UPD145',
            'Model': 'Sedan'
        }

        response = self.client.put(reverse('base:vehicles'), data=updated_vehicle_data, content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Updated Successfully')

        # Verify that the vehicle was updated in the database
        updated_vehicle = Vehicle.objects.get(pk=1)
        self.assertEqual(updated_vehicle.RegistrationNumber, 'UPD145')
        self.assertEqual(updated_vehicle.Model, 'Sedan')'''

    def test_delete_vehicle(self):
        # Create a vehicle to delete
        vehicle = Vehicle.objects.create(VehicleID=1, RegistrationNumber='ONT123', Model='SUV', Capacity=4)

        response = self.client.delete(reverse('base:removeVehicle', kwargs={'vehicle_id': vehicle.pk}), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Deleted Successfully')

        # Verify that the vehicle was deleted from the database
        self.assertEqual(Vehicle.objects.count(), 0)

    def test_request_page_with_valid_parameters(self):
        # Prepare test data
        params = {
            'origin': 'Waterloo',
            'destination': 'Kitchener',
            'mybtn': 'submit',  # Simulate button click
        }

        url = reverse('base:route_planning')

        # Make a GET request with the parameters
        response = self.client.get(url, params)

        # Assert response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_get_all_drivers(self):
        response = self.client.get(reverse('base:addDriver'))  
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), Driver.objects.count())

    def test_add_driver(self):
        address_Data = {
            'AddressID' : 1,
            'Street': '90 Forfar Ave',
            'City': 'Kitchener', 
            'Province': 'Ontario',
            'ZIPCode': 'N2P2Z8',
            'Country': 'Toronto'}
        driver_Data = {
            'DriverID': 1,
            'DriverName': 'John Doe',
            'MobileNumber': '5648886750',
            'LicenseNumber': 'N67Cuk8478',
            'Salary': 3457.00
        }
        role_Data = {
            'RoleID' : 1,
            'RoleName': 'Driver'}
        
        response = self.client.post(reverse('base:addDriver'), data={
            'DriverData': driver_Data,
            'AddressData': address_Data
            #'RoleData': role_Data,
        }, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json().get('message'), 'Driver added successfully.')

    '''def test_update_driver(self):
        driver = Driver.objects.create(name='Test Driver', age=25)
        new_name = 'Updated Driver Name'
        driver_data = {'DriverID': driver.DriverID, 'name': new_name}

        response = self.client.put(f'/api/drivers/{driver.DriverID}/', json.dumps(driver_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Updated Successfully')

        updated_driver = Driver.objects.get(DriverID=driver.DriverID)
        self.assertEqual(updated_driver.name, new_name)

    def test_delete_driver(self):
        driver = Driver.objects.create(name='Driver to Delete', age=30)

        response = self.client.delete(f'/api/drivers/{driver.DriverID}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'Deleted Successfully')
        self.assertFalse(Driver.objects.filter(DriverID=driver.DriverID).exists())'''


