from django.test import TestCase
from django.core.urlresolvers import reverse


class UserListViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('user_list')
        self.response = self.client.get(self.url)

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template_used(self):
        self.assertTemplateUsed('account/user_list.htm')
