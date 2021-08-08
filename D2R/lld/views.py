from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def error_404_view(request, exception):
    return render(request, '404.html')
