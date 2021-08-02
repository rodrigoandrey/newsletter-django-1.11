import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


# Metodo de Normalização de numero de telefone para inserção no DB
def normalize_phone(phone):
    for ch in ['(', ')', '-', ' ']:
        phone = phone.replace(ch, '')
    return phone


# Metodo de Validação de tamanho minimo
def validate_len(value):
    if value is None:
        raise ValidationError(_("Este campo é obrigatorio."))
    if len(value) < 2:
        raise ValidationError(_("Este campo precisa ter mais de 2 caracteres."))
    return value


# Metodo de Validação para previnir caracteres especiais
def validate_char(value):
    if not re.match("^[' A-Za-z0-9_-]+$", value):
        raise ValidationError(_("Este campo não pode conter caracteres especiais."))
    return value
