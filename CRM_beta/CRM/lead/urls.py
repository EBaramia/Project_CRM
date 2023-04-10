from django.urls import path
from .views import LeadCreateView, LeadDeleteView, LeadUpdateView, ConvertToClientView, LeadDeatailView, LeadListView

app_name = 'lead'

urlpatterns = [
    path('', LeadListView.as_view(), name='leads_list'),
    path('<int:pk>/', LeadDeatailView.as_view(), name='leads_detail'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='leads_delete'),
    path('<int:pk>/edit/', LeadUpdateView.as_view(), name='leads_edit'),
    path('<int:pk>/convert/', ConvertToClientView.as_view(), name='leads_convert'),
    path('add-lead/', LeadCreateView.as_view(), name='add_lead'),
]
