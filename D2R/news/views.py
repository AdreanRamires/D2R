from django.shortcuts import render

from D2R.news.models import NewsModel


def latest_news(request):
    news = NewsModel.objects.all()

    context = {
        'news': news,
    }

    return render(request, 'news.html', context=context)


def read_more(request, pk):
    new = NewsModel.objects.get(pk=pk)

    context = {
        'new': new,
    }

    return render(request, 'read-more.html', context=context)
