from django.urls import path
from .views import index, personas, detallepersona, crearpersona, modificar, eliminar, asignar_mancuerna, crear_mancuerna, lista_mancuernas
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('personas/', personas, name='personas'),
    path('detallepersona/<id>', detallepersona, name='detallepersona'),
    path('crearpersona/', crearpersona, name='crearpersona'),
    path('modificar/<id>', modificar, name='modificar'),
    path('eliminar/<id>', eliminar, name='eliminar'),
    path('mancuernas/', lista_mancuernas, name='lista_mancuernas'),
    path('mancuernas/crear/', crear_mancuerna, name='crear_mancuerna'),
    path('mancuernas/asignar/<int:id>/', asignar_mancuerna, name='asignar_mancuerna'),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)