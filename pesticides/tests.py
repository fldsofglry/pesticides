from django.test import TestCase
from django.urls import reverse

class RecordIndexViewTests(TestCase):
    def test_no_records(self):
        response = self.client.get(reverse("pesticides:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No records found.")
        # using assertQuerysetEqual, but is deprecated since v4.2
        # should use assertQuerySetEqual() when upgraded to 4.2
        self.assertQuerysetEqual(response.context["latest_records_list"], [])