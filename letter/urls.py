from django.conf.urls import url
from letter.views import HomeTemplateView, SubscribersCreateView, SubscribersListView

urlpatterns = [
    url(r'^$', HomeTemplateView.as_view(), name='home'),
    url(r'^newsletter/', SubscribersCreateView.as_view(), name='newsletter'),
    url(r'^subscribers/', SubscribersListView.as_view(), name='subscribers')
]
