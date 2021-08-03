from django.urls import path

from D2R.users.views import login_user, logout_user, register_user, profile_user

urlpatterns = [
    path('login/', login_user, name='login user'),
    path('logout/', logout_user, name='logout user'),
    path('register/', register_user, name='register user'),
    path('user-profile/', profile_user, name='profile user'),
]
