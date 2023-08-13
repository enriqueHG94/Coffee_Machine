import unittest

from main import is_resource_sufficient


class TestCoffeeMachine(unittest.TestCase):
    def test_is_resource_sufficient(self):
        # Test when resources are sufficient
        order_ingredients = {"water": 50, "coffee": 18}
        self.assertTrue(is_resource_sufficient(order_ingredients))

        # Test when resources are insufficient
        order_ingredients = {"water": 400, "coffee": 18}
        self.assertFalse(is_resource_sufficient(order_ingredients))

        # Test when only one resource is insufficient
        order_ingredients = {"water": 50, "coffee": 200}
        self.assertFalse(is_resource_sufficient(order_ingredients))
