
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import page.views
import page.urls
import information.views
import information.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('page.urls')),
    path('information/',include('information.urls')),
]