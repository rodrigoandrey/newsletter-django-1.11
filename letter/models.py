from django.db import models
from django.core.validators import validate_email
from newsletter.validators import normalize_phone, validate_len, validate_char
from django.utils.translation import ugettext_lazy as _


# Modelo base criacao/atualizacao e status.
class BaseMixin(models.Model):
    created_at = models.DateTimeField(_('Criado em'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Atualizado em'), auto_now=True)
    status = models.BooleanField(_('Ativo'), default=True)

    class Meta:
        abstract = True


# Modelo de inscritos
class Subscribers(BaseMixin):
    REASON_CHOICES = (
        ('Motivo 01', _('Motivo 01')),
        ('Motivo 02', _('Motivo 02')),
        ('Motivo 03', _('Motivo 03')),
    )

    name = models.CharField(_('Nome'), max_length=30, null=False, blank=False,
                            validators=[validate_char, validate_len])
    lastname = models.CharField(_('Sobrenome(s)'), max_length=30, null=False, blank=False,
                                validators=[validate_char, validate_len])
    email = models.EmailField(_('Email'), null=False, blank=False, unique=True,
                              validators=[validate_email])
    phone = models.CharField(_('Telefone'), max_length=15, null=True, blank=True)
    reason = models.CharField(_('Motivo da Inscrição'), max_length=20, null=True, blank=True,
                              choices=REASON_CHOICES)

    # Method para normalizar dados antes de inserir no banco.
    def save(self, *args, **kwargs):
        if self.phone:
            self.phone = normalize_phone(self.phone)
        self.name = self.name.title()
        self.lastname = self.lastname.title()
        self.email = self.email.lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _('Inscrito')
        verbose_name_plural = _('Inscritos')


class News(BaseMixin):
    categoria = models.CharField(_('Categoria'), max_length=50, null=True, blank=True)
    title = models.CharField(_('Titulo'), max_length=255, null=False, blank=False)
    sub_title = models.CharField(_('Sub-Titulo'), max_length=255, null=True, blank=True)
    text = models.TextField(_('Texto'), null=False, blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Noticia')
        verbose_name_plural = _('Noticias')
