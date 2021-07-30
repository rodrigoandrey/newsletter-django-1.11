from django.conf.urls import url
from letter.views import SubscribersCreateView, SubscribersListView

urlpatterns = [
    url(r'^newsletter/', SubscribersCreateView.as_view(), name='index'),
    url(r'^subscribers/', SubscribersListView.as_view(), name='subscribers')
]
