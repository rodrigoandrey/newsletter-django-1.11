from django.db import models


class BaseMixin(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    status = models.BooleanField('Ativo', default=True)

    class Meta:
        abstract = True


# usuário precisa inserir - Nome, sobrenome, e-mail, telefone, Motivo de inscrição.
class NewsLetter(BaseMixin):
    name = models.CharField('Nome', max_length=80, null=False, blank=False)
    lastname = models.CharField('Sobrenome', max_length=80, null=False, blank=False)
    email = models.EmailField('Email', null=False, blank=False, unique=True)
    phone = models.CharField('Telefone', max_length=15, null=True, blank=True)
    reason = models.CharField('Motivo de Inscrição', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Newsletter'
        verbose_name_plural = 'Newsletters'
