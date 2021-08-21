from django.urls import path

from . import views

app_name = 'schedule'

urlpatterns = [
    path('test1', views.test1, name='test1'),
    path('test2', views.test2, name='test2'),
    path('test3', views.test3, name='test3'),
]