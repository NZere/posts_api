from django.urls import path
from . import views


urlpatterns = [
    path('user/login', views.login_view, name='login'),
    path('user/logout', views.logout_view, name='logout'),
    path('user/register', views.register_view, name='register_user'),
]