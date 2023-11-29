from django.test import TestCase
from django.urls import reverse

class RecordIndexViewTests(TestCase):
    def test_index_page_load(self):
        response = self.client.get(reverse("pesticides:index"))
        self.assertEqual(response.status_code, 200)

    def test_no_records(self):
        response = self.client.get(reverse("pesticides:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No records found.")
        # using assertQuerysetEqual, but is deprecated since v4.2
        # should use assertQuerySetEqual() when upgraded to 4.2
        self.assertQuerysetEqual(response.context["latest_records_list"], [])

class RecordDetailViewTests(TestCase):
    def test_record_detail_page_load(self):
        response = self.client.get(reverse("pesticides:detail", args="13"))
        self.assertEqual(response.status_code, 200)  

class FormulaIndexViewTests(TestCase):
    def test_formula_index_page_load(self):
        response = self.client.get(reverse("pesticides:formula"))
        self.assertEqual(response.status_code, 200)

    def test_no_records(self):
        response = self.client.get(reverse("pesticides:formula"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No records found.")
        # using assertQuerysetEqual, but is deprecated since v4.2
        # should use assertQuerySetEqual() when upgraded to 4.2
        self.assertQuerysetEqual(response.context["formulas"], [])

class FormulaDetailViewTests(TestCase):
    def test_record_detail_page_load(self):
        response = self.client.get(reverse("pesticides:formula_detail", args="1"))
        self.assertEqual(response.status_code, 200)  