from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField, UserCreationForm
from django.utils.translation import ugettext_lazy as _
from accounts.models import CustomUserModel, BasicProfileModel, AddressModel, SocialNetworkModel


class CustomUserCreationForm(UserCreationForm, forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'autofocus': True, 'placeholder': _('Nome')})
        self.fields['last_name'].widget.attrs.update({'autofocus': False, 'placeholder': _('Sobrenome(s)')})
        self.fields['email'].widget.attrs.update({'autofocus': False, 'placeholder': _('email@exemplo.com.br')})
        self.fields['password1'].widget.attrs.update({'autofocus': False, 'placeholder': _('Senha')})
        self.fields['password2'].widget.attrs.update({'autofocus': False, 'placeholder': _('Repita a Senha')})

    class Meta:
        model = CustomUserModel
        fields = ('first_name', 'last_name', 'email', )

    # password1 = forms.CharField(label='Senha', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Repita a Senha', widget=forms.PasswordInput)

    def save(self, commit=True):
        user = super(CustomUserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password1'))
        user.username = self.cleaned_data['email']
        if commit:
            user.save()

        return user


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = CustomUserModel
        fields = ('first_name', 'last_name', 'email',  'is_active', 'is_staff', )

    password = ReadOnlyPasswordHashField()

    def clean_password(self):
        return self.initial['password']


class BasicProfileForm(forms.ModelForm):
    class Meta:
        model = BasicProfileModel
        fields = ('profile_picture',)


class SocialNetworkForm(forms.ModelForm):
    class Meta:
        model = SocialNetworkModel
        fields = ('link',)


class AddressForm(forms.ModelForm):
    class Meta:
        model = AddressModel
        fields = ('address',)
