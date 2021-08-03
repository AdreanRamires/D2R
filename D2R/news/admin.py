from django.contrib import admin
from D2R.news.models import NewsModel


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    pass
