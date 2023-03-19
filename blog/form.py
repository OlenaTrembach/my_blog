from django import forms
from .models import Comments


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('text_comment', 'name', 'email')


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Поиск...'
            }
        )
    )

