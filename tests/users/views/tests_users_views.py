from D2R.users.models import Profile
from tests.global_test_setup import GlobalTestSetup
from django.urls import reverse


class UsersViewsTests(GlobalTestSetup):

    def setUp(self):
        super().setUp()

    def test_login_user_GET(self):
        response = self.client.get(reverse('login user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertIn('form', response.context)

    def test_login_user_POST(self):
        response = self.client.post(reverse('login user'), data=self.credentials, follow=True)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertRedirects(response, '/', 302)

    def test_register_user_GET(self):
        response = self.client.get(reverse('register user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')
        self.assertIn('form', response.context)

    def test_register_user_POST(self):
        response = self.client.post(reverse('register user'), data=self.new_user_credentials, follow=True)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertRedirects(response, '/', 302)

    def test_logout_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('logout user'))
        self.assertRedirects(response, '/', 302)

    def test_profile_user_GET(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/user-profile.html')
        self.assertIn('form', response.context)

    def test_profile_user_POST(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('profile user'),
                                    data={'profile_image': self.image_obj, })
        self.assertRedirects(response, '/users/user-profile/', 302)
