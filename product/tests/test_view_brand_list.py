from unittest import skip

from django.test import TestCase
from django.core.urlresolvers import reverse


class BrandSearchableListViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('brand_list')
        self.response = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed(self.response, 
                                'product/brand_list.html')

    @skip('todo')
    def test_filter(self):
        pass
