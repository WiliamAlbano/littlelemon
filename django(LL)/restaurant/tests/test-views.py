# tests/test_views.py

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from models import Menu
from serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Create a few instances of the Menu model for testing
        self.menu_item1 = Menu.objects.create(
            name="Pizza", 
            description="Delicious cheese pizza", 
            price=12.99
        )
        self.menu_item2 = Menu.objects.create(
            name="Burger", 
            description="Juicy beef burger", 
            price=8.99
        )
        self.menu_item3 = Menu.objects.create(
            name="Pasta", 
            description="Creamy Alfredo pasta", 
            price=10.49
        )
        self.client = APIClient()

    def test_getall(self):
        # Send a GET request to retrieve all Menu objects
        response = self.client.get('/api/menu/')  # Assuming the URL pattern is set correctly

        # Serialize the data to compare with the response
        expected_data = MenuSerializer([self.menu_item1, self.menu_item2, self.menu_item3], many=True).data
        
        # Check if the response is successful
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert if the serialized data equals the response data
        self.assertEqual(response.data, expected_data)
