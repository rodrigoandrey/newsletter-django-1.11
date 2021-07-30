from django.contrib import admin
from letter.models import Subscribers


class SubscribersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'email', 'phone', 'created_at', 'status', )
    list_display_links = ('name', 'lastname', 'email', )
    search_fields = ('id', 'name', 'email',)
    list_per_page = 10


admin.site.register(Subscribers, SubscribersAdmin)
