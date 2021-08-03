from django import forms

from D2R.news.models import NewsModel


class NewsForm(forms.ModelForm):
    class Meta:
        model = NewsModel
        exclude = ('posted_on',)
