from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import CustomUserModel
from accounts.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUserModel
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ('id', 'email', 'first_name', 'last_name', 'is_superuser', 'is_active',)
    list_display_links = ('id', 'email', )
    list_filter = ('is_staff', 'is_active')
    list_editable = ('is_active',)

    fieldsets = (
        ('Credenciais', {'fields': ('email', 'password',)}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'first_name', 'last_name', 'password1', 'password2')
        }),
    )
    search_fields = ('email', 'first_name', 'last_name',)
    readonly_fields = ('last_login', 'date_joined', )
    ordering = ('id', )
    filter_horizontal = ('user_permissions',)
    list_per_page = 20


admin.site.register(CustomUserModel, CustomUserAdmin)
