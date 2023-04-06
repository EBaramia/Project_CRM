from django.urls import path
from .views import dachboard

app_name = 'dashboard'

urlpatterns = [
    path('', dachboard, name='dashboard'),
]
