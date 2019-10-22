from django.urls import path

from . import views

urlpatterns = [
    path('data_get', views.data_get, name='data'),
    path('data_post', views.data_post, name='data'),
]
