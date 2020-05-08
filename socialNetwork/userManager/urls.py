from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('add_user', views.add_user, name='add_user'),
    path('add_user_service', views.add_user_service, name='add_user_service'),
]
