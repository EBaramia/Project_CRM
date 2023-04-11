from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import signup
from userprofile.forms import LoginForm

app_name = 'userprofile'

urlpatterns = [
    path('sign-up/', signup, name='signup'),
    path('log-in/', LoginView.as_view(template_name='userprofile/login_page.html',
         authentication_form=LoginForm), name='login'),
    path('log-out/', LogoutView.as_view(template_name='userprofile/login_page.html'), name='logout'),
]
