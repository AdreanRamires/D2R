from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.core.files.uploadedfile import SimpleUploadedFile
from D2R.gallery.models import ImageModel
from D2R.news.models import NewsModel

UserModel = get_user_model()


class GlobalTestSetup(TestCase):

    def setUp(self):
        self.client = Client(
        )
        self.user = UserModel.objects.create_user(
            email='test@abv.bg',
            password='123')
        self.credentials = {
            'username': 'test@abv.bg',
            'password': '123',
        }
        self.new_user_credentials = {
            'email': 'test1@abv.bg',
            'password1': '123',
            'password2': '123',
        }
        self.image = SimpleUploadedFile(
            name='login-avatar.png',
            content=open('D:/D2R/static/images/login-avatar.png', 'rb').read(),
        )
        self.image_obj = ImageModel.objects.create(
            title='test',
            description='test',
            image=self.image,
            user_id=self.user.id,
        )
        self.new = NewsModel.objects.create(
            title='test title',
            post_title='test post title text',
            about='test about text',
            image=self.image,
            posted_on='day/month/year',
        )
