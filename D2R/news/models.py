from django.core.validators import MinValueValidator
from django.db import models


class NewsModel(models.Model):
    title = models.CharField(
        max_length=242,
        blank=False,
    )

    post_title = models.CharField(
        max_length=74,
        blank=False,
    )

    about = models.TextField(
        blank=False,
    )

    image = models.ImageField(
        blank=False,
        upload_to='media/news',
    )

    posted_on = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.title
