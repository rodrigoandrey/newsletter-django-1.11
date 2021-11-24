from django.conf.urls import url
from django.contrib.auth import views as auth_views
from accounts.views import UserProfile, user_register

urlpatterns = [
    url(r'^register/', user_register, name='register'),
    url(r'^login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
    url(r'^profile/', UserProfile.as_view(), name='profile'),
]
