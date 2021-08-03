from django.contrib import admin
from D2R.gallery.models import ImageModel


@admin.register(ImageModel)
class GalleryAdmin(admin.ModelAdmin):
    pass
