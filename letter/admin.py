from django.contrib import admin
from letter.models import Subscribers, News
from modeltranslation.admin import TranslationAdmin


class SubscribersAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at', 'id')
    fields = ('id', 'name', 'lastname', 'email', 'phone', 'reason', 'status', 'created_at', 'updated_at')
    list_display = ('id', 'name', 'lastname', 'email', 'phone', 'reason', 'created_at', 'status', )
    list_display_links = ('name', 'lastname', 'email', )
    list_editable = ('status', )
    search_fields = ('id', 'name', 'email', 'reason')
    list_per_page = 20


admin.site.register(Subscribers, SubscribersAdmin)


class NewsAdmin(TranslationAdmin):
    fields = ['id', 'categoria', 'title', 'sub_title', 'text']
    readonly_fields = ['id']
    list_display = ['id', 'title', 'created_at', 'status']
    list_display_links = ['id', 'title']
    list_editable = ['status']
    search_fields = ['id', 'title']
    list_per_page = 20


admin.site.register(News, NewsAdmin)
