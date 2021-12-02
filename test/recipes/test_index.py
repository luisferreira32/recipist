from django.test import TestCase
from django.urls import reverse

class RecipeIndexViewTests(TestCase):
    def test_no_recipes(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('recipes:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No recipes are available.")
        self.assertQuerysetEqual(response.context['recipes_list'], [])