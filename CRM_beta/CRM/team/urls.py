from django.urls import path
from .views import edit_team, detail, teams_list, teams_activate

app_name = 'team'

urlpatterns = [
    path('', teams_list, name='team_list'),
    path('<int:pk>/edit/', edit_team, name='edit_team'),
    path('<int:pk>/activate/', teams_activate, name='activate'),
    path('<int:pk>/', detail, name='detail'),
]
