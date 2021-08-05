from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ImageForm, ImageEditForm
from .models import ImageModel


def gallery(request):
    context = {
        'images': ImageModel.objects.all(),
    }

    return render(request, 'gallery/gallery.html', context=context)


@login_required
def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect('gallery')

    else:
        form = ImageForm()

        context = {
            'form': form,
        }

        return render(request, 'gallery/image-upload.html', context=context)


def image_details(request, pk):
    image = ImageModel.objects.get(pk=pk)
    creator = request.user.id == image.user.id
    super_user = request.user.is_superuser
    context = {
        'image': image,
        'creator': creator,
        'super_user': super_user,
    }

    return render(request, 'gallery/image-details.html', context=context)


@login_required()
def image_edit(request, pk):
    image = ImageModel.objects.get(pk=pk)
    if request.method == 'POST':
        form = ImageEditForm(request.POST, instance=image)
        if form.is_valid():
            form.save()
            return redirect('image details', image.id)

    else:
        form = ImageEditForm(instance=image)

    context = {
        'form': form,
        'image': image,
        }

    return render(request, 'gallery/image-edit.html', context=context)


@login_required()
def image_delete(request, pk):
    image = ImageModel.objects.get(pk=pk)
    if request.method == 'POST':
        image.image.delete()
        image.delete()
        return redirect('gallery')

    else:

        context = {
            'image': image,
        }

        return render(request, 'gallery/image-delete.html', context=context)
