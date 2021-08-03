from django.urls import path
from .views import gallery, image_upload, image_details, image_edit, image_delete

urlpatterns = [
    path('', gallery, name='gallery'),
    path('upload/', image_upload, name='image upload'),
    path('image-details/<int:pk>', image_details, name='image details'),
    path('image-edit/<int:pk>', image_edit, name='image edit'),
    path('image-delete/<int:pk>', image_delete, name='image delete'),
]
