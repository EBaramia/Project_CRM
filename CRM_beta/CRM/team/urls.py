from django.urls import path
from .views import edit_team

app_name = 'team'

urlpatterns = [
    path('<int:pk>/edit/', edit_team, name='edit_team')
]
