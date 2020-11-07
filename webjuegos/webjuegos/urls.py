from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalogo/',include('catalogo.urls'))
]

urlpatterns+= static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)