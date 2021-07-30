from django.db import models
from letter.validators import validate_phone


class BaseMixin(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    status = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


# Usuário precisa inserir - Nome, sobrenome, e-mail, telefone, Motivo de inscrição.
class Subscribers(BaseMixin):
    name = models.CharField('Nome', max_length=80, null=False, blank=False)
    lastname = models.CharField('Sobrenome', max_length=80, null=False, blank=False)
    email = models.EmailField('Email', null=False, blank=False, unique=True)
    phone = models.CharField('Telefone', max_length=15, null=True, blank=True)
    reason = models.CharField('Motivo da Inscrição', max_length=100, null=True, blank=True)

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
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'
