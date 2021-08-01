from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

char_list = ['!', '@', '#', '%', '&', '*', '#', '(', ')', '_', '+', '=', '{', '[', '}', ']', '|', '\\', ';', ':', '"',
             '<', '>', '?', '/']


def validate_phone(phone):
    for ch in ['(', ')', '-', ' ']:
        phone = phone.replace(ch, '')
    return phone


def validate_len(value):
    if len(value) < 2:
        raise ValidationError(_("Este campo precisa ter mais de 2 caracteres."))
    return value


def validate_char(value):
    for ch in char_list:
        if ch in value:
            raise ValidationError(_("Este campo não pode conter caracteres especiais."))
    return value
