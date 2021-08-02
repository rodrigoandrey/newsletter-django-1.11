from django.conf.urls import url
from letter.views import HomeTemplateView, SubscribersListView, subscriber_register

urlpatterns = [
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^newsletter/', subscriber_register, name='newsletter'),
    url(r'^subscribers/', SubscribersListView.as_view(), name='subscribers'),
]
