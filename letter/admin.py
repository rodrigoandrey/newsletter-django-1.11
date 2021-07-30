from django.contrib import admin
from letter.models import NewsLetter


class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lastname', 'email', 'created_at', 'status', )
    list_display_links = ('name', 'lastname', 'email', )
    search_fields = ('id', 'name', 'email',)
    list_per_page = 30


admin.site.register(NewsLetter, NewsLetterAdmin)
