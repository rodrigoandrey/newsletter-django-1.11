from django import forms
from letter.models import Subscribers
from django.utils.translation import ugettext_lazy as _


class SubscribersForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'autofocus': True, 'placeholder': _('Nome')})
        self.fields['lastname'].widget.attrs.update({'placeholder': _('Sobrenome(s)')})
        self.fields['phone'].widget.attrs.update({'placeholder': _('Telefone')})
        self.fields['email'].widget.attrs.update({'placeholder': _('exemplo@dominio.com')})

    class Meta:
        model = Subscribers
        fields = (
            'name',
            'lastname',
            'phone',
            'email',
            'reason',
        )
