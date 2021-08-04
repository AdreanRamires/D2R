from django.db import models

from D2R.users.models import DrUser


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
        upload_to='media/gallery',
        blank=False,

    )

    user = models.ForeignKey(DrUser, on_delete=models.CASCADE)
