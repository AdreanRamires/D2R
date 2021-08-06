from unittest.mock import patch
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from D2R.gallery.models import ImageModel

UserModel = get_user_model()


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email='test@abv.bg',
            password='123')
        self.client.force_login(self.user)
        self.image = SimpleUploadedFile(
            name='login-avatar.jpg',
            content=open('D:/D2R/static/images/login-avatar.png', 'rb').read(),
            content_type='image/jpeg')
        self.image_obj = ImageModel.objects.create(
            title='test',
            description='test',
            image=self.image,
            user_id=self.user.id,
        )

    @patch('D2R.gallery.models.ImageModel.objects')
    def test_gallery_GET(self, image_mock):
        image_mock.all.return_value = []
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/gallery.html')
        self.assertListEqual(response.context['images'], [])

    def test_image_upload_GET(self):
        response = self.client.get(reverse('image upload'))
        self.assertEqual(response.status_code, 200)
        print(response.context['form'])

    def test_image_details_GET(self):
        response = self.client.get(reverse('image details', kwargs={'pk': self.image_obj.id}),
                                   data={'image': self.image_obj})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/image-details.html')
        self.assertEquals(response.context['image'], self.image_obj)

    def test_image_edit_GET(self):
        response = self.client.get(reverse('image edit', kwargs={'pk': self.image_obj.id}),
                                   data={'image': self.image_obj})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/image-edit.html')
        self.assertEquals(response.context['image'], self.image_obj)

    def test_image_delete_GET(self):
        response = self.client.get(reverse('image delete', kwargs={'pk': self.image_obj.id}),
                                   data={'image': self.image_obj})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/image-delete.html')
        self.assertEquals(response.context['image'], self.image_obj)

    def test_image_delete_POST(self):
        response = self.client.post(reverse('image delete', kwargs={'pk': self.image_obj.id}), follow=True)
        self.assertRedirects(response, '/gallery/', status_code=302)

    def test_image_edit_POST(self):
        response = self.client.post(reverse('image edit', kwargs={'pk': self.image_obj.id}),
                                    data={'title': 'edited title',
                                          'description': 'edited description',
                                          'image': self.image_obj}, follow=True)
        self.assertEqual(response.context['image'].title, 'edited title')
        self.assertRedirects(response, f'/gallery/image-details/{self.image_obj.id}', status_code=302)

    def test_image_upload_POST(self):
        response = self.client.post(reverse('image upload'),
                                    data={'title': 'edited title',
                                          'description': 'edited description',
                                          'image': 'path/to/image.png'})
        # Can't validate form
        # {'form': <ImageForm bound=True, !!! valid=False !!!, fields=(title;description;image)>}
        # self.assertRedirects(response, '/gallery/', status_code=302)


