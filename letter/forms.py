from django import forms
from letter.models import Subscribers
from letter.validators import validate_phone


class SubscribersForm(forms.ModelForm):
    class Meta:
        model = Subscribers
        fields = (
            'name',
            'lastname',
            'email',
            'phone',
            'reason',
        )