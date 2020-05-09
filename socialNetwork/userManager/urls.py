from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('sign_up', views.add_user, name='sign_up'),
    path('add_user_service', views.add_user_service, name='add_user_service'),
]
