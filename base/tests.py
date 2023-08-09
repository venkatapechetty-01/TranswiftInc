from django.test import TestCase
from django.urls import reverse
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Vehicle
from .serializers import VehicleSerializer
from .views import vehicleApi

class VehicleApiTest(TestCase):
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

