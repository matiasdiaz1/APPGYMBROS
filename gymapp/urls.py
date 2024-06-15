from django.urls import path
from .views import index, personas, detallepersona, crearpersona, modificar, eliminar
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('personas/', personas, name='personas'),
    path('detallepersona/<id>', detallepersona, name='detallepersona'),
    path('crearpersona/', crearpersona, name='crearpersona'),
    path('modificar/<id>', modificar, name='modificar'),
    path('eliminar/<id>', eliminar, name='eliminar'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)