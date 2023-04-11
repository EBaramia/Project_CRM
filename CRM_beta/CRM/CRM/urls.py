from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from userprofile.views import my_account


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core_app.urls')),
    path('', include('userprofile.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard/leads/', include('lead.urls')),
    path('dashboard/teams/', include('team.urls')),
    path('dashboard/clients/', include('client_app.urls')),
    path('dashboard/my-acount/', my_account, name='acount'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
