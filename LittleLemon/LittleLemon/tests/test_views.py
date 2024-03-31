from django.test import TestCase, Client
from restaurant.models import Menu

client = Client()
# Testcase class 1
class MenuItemViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        cls.item2 = Menu.objects.create(title="French fries", price=13, inventory=40)
        # cls.item = Menu.objects.create(title="French fries", price=13, inventory=40)
        # response = c.post('restaurant/menu', {'title': 'Pie', 'price': 4.5, 'inventory':8})
        # self.assertEqual(response.status_code, 201)

    # def test_view_url_exists(self):
    #     response = self.client.get('restaurant/menu/')
    #     # response2 = self.client.post('restaurant/menu/', {'title': 'Pie', 'price': 4.5, 'inventory':8})
    #     self.assertEqual(response.status_code, 200)
    #     # self.assertEqual(response2.status_code, 201)
    def test_getall(self):
        item = Menu.objects.all()
        count = 0
        for i in item:
            count +=1
        self.assertEqual(count, 2)

    def test_fields(self):
        self.assertIsInstance(self.item.title, str)