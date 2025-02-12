# tests/test-models.py

from django.test import TestCase
from models import Menu

class MenuTest(TestCase):
    def test_str_method(self):
        # Create an instance of the Menu model
        menu_item = Menu.objects.create(
            name="Pizza", 
            description="Delicious cheese pizza", 
            price=12.99
        )

        # Define the expected string representation
        expected_str = "Pizza - $12.99"

        # Use assertEqual to compare the actual string representation
        self.assertEqual(str(menu_item), expected_str)
