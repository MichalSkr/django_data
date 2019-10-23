from django.urls import path

from . import views

urlpatterns = [
    path('data_get', views.data_get, name='data'),
    path('data_post', views.data_post, name='data_post'),
    path('data_browse', views.data_browse, name='data_browse'),
    path('data_get_specific', views.data_get_specific, name='data_get_specific'),
    path('upload_data_file', views.upload_data_file, name='upload_data_file')
]
