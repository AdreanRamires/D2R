from django.contrib.auth import get_user_model
from django.db import models
UserModel = get_user_model()


class ImageModel(models.Model):
    title = models.CharField(
        max_length=15,
        blank=False,
    )

    description = models.TextField(
        max_length=254,
        blank=False,
    )

    image = models.ImageField(
        upload_to='media/profiles',
        blank=False,
    )

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
