from django import forms
from .models import ImageModel


class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        exclude = ('user',)
        widgets = {'title': forms.TextInput(attrs={'class': 'input'}),
                   'description': forms.Textarea(attrs={'class': 'input',
                                                        'style': 'height:250px'}),
                   }


class ImageEditForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        exclude = ('image', 'user',)
        widgets = {'title': forms.TextInput(attrs={'class': 'input'}),
                   'description': forms.Textarea(attrs={'class': 'input',
                                                        'style': 'height:250px'}),
                   }

