from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^grappelli/', include('grappelli.urls')),  # grappelli URLS
    url(r'^admin/', admin.site.urls, name='admin'),
    url(r'^', include('letter.urls')),
    url(r'^accounts/', include('accounts.urls')),
]


