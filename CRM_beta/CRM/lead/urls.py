from django.urls import path
from .views import AddFileView, AddCommentView, LeadCreateView, LeadDeleteView, LeadUpdateView, ConvertToClientView, LeadDetailView, LeadListView

app_name = 'lead'

urlpatterns = [
    path('', LeadListView.as_view(), name='leads_list'),
    path('<int:pk>/', LeadDetailView.as_view(), name='leads_detail'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='leads_delete'),
    path('<int:pk>/edit/', LeadUpdateView.as_view(), name='leads_edit'),
    path('<int:pk>/convert/', ConvertToClientView.as_view(), name='leads_convert'),
    path('<int:pk>/add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('<int:pk>/add_file/', AddFileView.as_view(), name='add_file'),
    path('add-lead/', LeadCreateView.as_view(), name='add_lead'),
]
