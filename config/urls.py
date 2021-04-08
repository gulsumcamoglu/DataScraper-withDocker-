from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from datascraper.views import product
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url('admin/', admin.site.urls),
    url('',include('datascraper.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)