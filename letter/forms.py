from django import forms
from letter.models import NewsLetter


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = NewsLetter
        fields = (
            'name',
            'lastname',
            'email',
            'phone',
            'reason',
        )
