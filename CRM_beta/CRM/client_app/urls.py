from django.urls import path
from .views import AddCommentView, ClientsListView, ClientDetailView, ClientCreateView, ClientDeleteView, ClientsUpdateView


app_name = 'client_app'

urlpatterns = [
    path('', ClientsListView.as_view(), name='clients_list'),
    path('<int:pk>', ClientDetailView.as_view(), name='clients_detail'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='clients_delete'),
    path('<int:pk>/edit/', ClientsUpdateView.as_view(), name='clients_edit'),
    path('<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('add/', ClientCreateView.as_view(), name='clients_add'),
]
