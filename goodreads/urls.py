from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from .view import landing_page,home_page

urlpatterns = [
    path('',landing_page,name='landing_page'),
    path('home/',home_page,name='home_page'),
    path('users/',include('users.urls')),
    path('books/',include('books.urls')),
    path('api/',include('api.urls')),
    path('api-auth/',include('rest_framework.urls')),
    path('admin/', admin.site.urls),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)