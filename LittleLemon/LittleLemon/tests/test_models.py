from django.test import TestCase
from restaurant.models import Menu

# Testcase class 1
class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        title = item.title
        price = item.price
        self.assertEqual(title, "IceCream")
        self.assertEqual(price, 80)
        self.assertNotEqual(item.inventory, 200)