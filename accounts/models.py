from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.core.validators import validate_email
from django.db import models
from newsletter.validators import validate_len, validate_char
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        if not email:
            raise ValueError("Email obrigatório.")
        if not password:
            raise ValueError("Senha obrigatória.")
        user = self.model(
            email=self.normalize_email(email),
            username=self.normalize_email(email),
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, username, password, **extra_fields)

    def create_staff_user(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Membro da equipe precisa ter is_staff = True')

        return self._create_user(email, username, password, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser = True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff = True')

        return self._create_user(email, username, password, **extra_fields)


class CustomUserModel(AbstractUser):
    class Meta:
        verbose_name = _('Usuário')
        verbose_name_plural = _('Usuários')

    email = models.EmailField(_('Email'), max_length=200, unique=True, blank=False, null=False,
                              validators=[validate_email])
    first_name = models.CharField(_('Nome'), max_length=100, blank=False, null=False,
                                  validators=[validate_char, validate_len])
    last_name = models.CharField(_('Sobrenome(s)'), max_length=200, blank=False, null=False,
                                 validators=[validate_char, validate_len])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name

    def get_short_name(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def save(self, *args, **kwargs):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()
        self.email = self.email.lower()
        super().save(*args, **kwargs)


class BasicProfileModel(models.Model):
    class Meta:
        verbose_name = _('Perfil de Usuário')
        verbose_name_plural = _('Perfis de Usuário')

    user = models.OneToOneField(CustomUserModel, on_delete=models.CASCADE, verbose_name=_('Usuário'))
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True,
                                        verbose_name=_('Foto de Perfil'), width_field=198, height_field=198)


class SocialNetworkModel(models.Model):
    class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'

    link = models.CharField('Rede Social', max_length=255, null=True, blank=True)
    user = models.ForeignKey(BasicProfileModel, on_delete=models.CASCADE, verbose_name='Perfil Usuário')

    def __str__(self):
        return self.user.email


class AddressModel(models.Model):
    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'

    address = models.CharField('Endereço', max_length=255, null=True, blank=True)
    user = models.ForeignKey(BasicProfileModel, on_delete=models.CASCADE, verbose_name='Perfil Usuário')

    def __str__(self):
        return self.user.email
