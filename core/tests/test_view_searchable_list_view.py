from unittest import skip
from django.test import TestCase
from django.test.client import RequestFactory

from core.tests.test_form_base_search_form import SingleFieldSearchForm
from core.views import SearchableListView

class MySearchableListView(SearchableListView):

    form_class = SingleFieldSearchForm


class SearchableListViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('/')
        self.view = MySearchableListView

    def test_get(self):
        response = self.view.as_view()(self.request)
        self.assertEqual(response.status_code, 200)