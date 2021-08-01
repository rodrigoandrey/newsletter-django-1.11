from django.db import models
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from letter.validators import validate_phone, validate_len, validate_char


class BaseMixin(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    status = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


# Usuário precisa inserir - Nome, sobrenome, e-mail, telefone, Motivo de inscrição.
class Subscribers(BaseMixin):
    REASON_CHOICES = (
        ('Motivo 01', 'Motivo 01'),
        ('Motivo 02', 'Motivo 02'),
        ('Motivo 03', 'Motivo 03'),
    )

    name = models.CharField('Nome', max_length=80, null=False, blank=False,
                            validators=[validate_char, validate_len])
    lastname = models.CharField('Sobrenome', max_length=80, null=False, blank=False,
                                validators=[validate_char, validate_len])
    email = models.EmailField('Email', null=False, blank=False, unique=True, validators=[validate_email])
    phone = models.CharField('Telefone', max_length=15, null=True, blank=True)
    reason = models.CharField('Motivo da Inscrição', max_length=20, null=True, blank=True,
                              choices=REASON_CHOICES)

    def save(self, *args, **kwargs):
        if self.phone:
            self.phone = validate_phone(self.phone)
        self.name = self.name.title()
        self.lastname = self.lastname.title()
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Inscrito'
        verbose_name_plural = 'Inscritos'
