from django.urls import path

from . import views

app_name = "list"

urlpatterns = [
    path('', views.home, name='index'),
    path('add', views.add, name='add'),
    path('edit', views.edit, name='edit'),
    path('delete', views.delete, name='delete'),
]