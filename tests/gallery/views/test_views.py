from unittest.mock import patch
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from D2R.users.models import DrUser
from D2R.gallery.models import ImageModel


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.image = SimpleUploadedFile(
            name='login-avatar.jpg',
            content=open('D:/D2R/static/images/login-avatar.png', 'rb').read(),
            content_type='image/jpeg')

    @patch('D2R.gallery.models.ImageModel.objects')
    def test_gallery_GET(self, image_mock):
        image_mock.all.return_value = []
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/gallery.html')
        self.assertListEqual(response.context['images'], [])

    def test_image_details_GET(self):
        user = DrUser.objects.create(
            email='test@abv.bg',
            password='123')

        user.save()

        image = ImageModel.objects.create(
            title='test',
            description='test',
            image=self.image,
            user_id=user.id,
        )
        image.save()

        response = self.client.get(reverse('image details',  kwargs={'pk': image.id}), data={'image': image}, follow=True)

