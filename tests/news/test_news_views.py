from tests.global_test_setup import GlobalTestSetup
from django.urls import reverse


class LldViewsTests(GlobalTestSetup):

    def test_latest_news_GET(self):
        response = self.client.get(reverse('news'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('news.html')

    def test_read_more_GET(self):
        response = self.client.get(reverse('news detail', kwargs={'pk': self.new.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'news/read-more.html')
        self.assertEqual(response.context['new'].title, 'test title')
