from django.contrib.auth import get_user_model
from tests.global_test_setup import GlobalTestSetup
from unittest.mock import patch
from django.urls import reverse

UserModel = get_user_model()


class GalleryViewsTests(GlobalTestSetup):

    def setUp(self):
        super().setUp()

    @patch('D2R.gallery.models.ImageModel.objects')
    def test_gallery_GET(self, image_mock):
        image_mock.all.return_value = []
        response = self.client.get(reverse('gallery'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/gallery.html')
        self.assertListEqual(response.context['images'], [])

    def test_image_upload_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('image upload'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('image-upload.html')

    def test_image_upload_POST(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('image upload'),
                                    data={'title': 'edited title',
                                          'description': 'edited description',
                                          'image': self.image_obj,
                                          'user': self.user
                                          })
        # Can't validate form
        # {'form': <ImageForm bound=True, !!! valid=False !!!, fields=(title;description;image)>}

    def test_image_details_GET(self):
        response = self.client.get(reverse('image details', kwargs={'pk': self.image_obj.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/image-details.html')
        self.assertEquals(response.context['image'], self.image_obj)

    def test_image_edit_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('image edit', kwargs={'pk': self.image_obj.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/image-edit.html')
        self.assertEquals(response.context['image'], self.image_obj)

    def test_image_edit_POST(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('image edit', kwargs={'pk': self.image_obj.id}),
                                    data={'title': 'edited title',
                                          'description': 'edited description'},
                                    follow=True)
        self.assertEqual(response.context['image'].title, 'edited title')
        self.assertRedirects(response, f'/gallery/image-details/{self.image_obj.id}', status_code=302)

    def test_image_delete_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('image delete', kwargs={'pk': self.image_obj.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery/image-delete.html')
        self.assertEquals(response.context['image'], self.image_obj)

    def test_image_delete_POST(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('image delete', kwargs={'pk': self.image_obj.id}), follow=True)
        self.assertRedirects(response, '/gallery/', status_code=302)
