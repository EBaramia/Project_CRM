from django.urls import path
from .views import clients_list, clients_detail, clients_add, clients_delete, clients_edit


app_name = 'client_app'

urlpatterns = [
    path('', clients_list, name='clients_list'),
    path('<int:pk>', clients_detail, name='clients_detail'),
    path('<int:pk>/delete/', clients_delete, name='clients_delete'),
    path('<int:pk>/edit/', clients_edit, name='clients_edit'),
    path('add/', clients_add, name='clients_add'),
]
