from django.test import Client, TestCase
from django.urls import reverse
from parameterized import parameterized
from rest_framework import status


client = Client()


class SearchAreaGetTest(TestCase):
    @parameterized.expand([
        [{'мясо': 250, 'огурец': 2},
         {'Салат «Русский»': 1}],
        [{'мясо': 500, 'огурец': 2, 'картофель': 3},
         {'Салат «Ленинградский»': 1, 'Салат «Русский»': 1}],
        [{'мясо': 1000, 'огурец': 7, 'картофель': 5},
         {'Салат «Ленинградский»': 1, 'Салат «Русский»': 3}],
        [{'рыба': 1600, 'картофель': 35, 'яйцо': 8},
         {'Салат с рыбой и овощами': 2}],
    ])
    def test_cook(self, data, expected_result):
        response = client.get(reverse('cookbook:what-can-i-cook'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data'], expected_result)
