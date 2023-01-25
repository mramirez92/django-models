from django.test import TestCase
from django.urls import reverse

class SnackTest(TestCase):

    def test_list_page_200(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        print('test snack_list status 200: pass')

    def test_list_page_template(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')
        self.assertTemplateUsed(response, 'base.html')
        print('test snack_templates: pass')
