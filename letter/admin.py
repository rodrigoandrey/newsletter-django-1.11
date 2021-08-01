from django.contrib import admin
from letter.models import Subscribers


class SubscribersAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'id')
    fields = ('id', 'name', 'lastname', 'email', 'phone', 'reason', 'status', 'created_at', 'updated_at')
    list_display = ('id', 'name', 'lastname', 'email', 'phone', 'reason', 'created_at', 'status', )
    list_display_links = ('name', 'lastname', 'email', )
    search_fields = ('id', 'name', 'email', 'reason')
    list_per_page = 10


admin.site.register(Subscribers, SubscribersAdmin)
