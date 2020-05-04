from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name="index"),
   path('stop/<id>', views.stop, name="stop"),
]
