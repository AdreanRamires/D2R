from tests.global_test_setup import GlobalTestSetup
from django.urls import reverse


class LldViewsTests(GlobalTestSetup):

    def test_lld_GET(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('index.html')
