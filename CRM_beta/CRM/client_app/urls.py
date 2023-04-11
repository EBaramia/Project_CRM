from django.urls import path
from .views import clients_expotr, AddFileView, AddCommentView, ClientsListView, ClientDetailView, ClientCreateView, ClientDeleteView, ClientsUpdateView


app_name = 'client_app'

urlpatterns = [
    path('', ClientsListView.as_view(), name='clients_list'),
    path('<int:pk>', ClientDetailView.as_view(), name='clients_detail'),
    path('<int:pk>/delete/', ClientDeleteView.as_view(), name='clients_delete'),
    path('<int:pk>/edit/', ClientsUpdateView.as_view(), name='clients_edit'),
    path('<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('<int:pk>/add_file/', AddFileView.as_view(), name='add_file'),
    path('add/', ClientCreateView.as_view(), name='clients_add'),
    path('export/', clients_expotr, name='export'),
]
