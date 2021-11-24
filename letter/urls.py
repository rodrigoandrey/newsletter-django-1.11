from django.conf.urls import url
from letter.views import HomeTemplateView, NewsTemplateView, subscriber_register, subscriber_view

urlpatterns = [
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^newsletter/', subscriber_register, name='newsletter'),
    url(r'^subscribers/', subscriber_view, name='subscribers'),
    url(r'^news/', NewsTemplateView.as_view(), name='news'),
]
