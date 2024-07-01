from django.urls import path
from .views import confirmacion, direccion_entrega, index, monedas, pago, personas, detallepersona, crearpersona, modificar, \
eliminar, asignar_mancuerna, crear_mancuerna, lista_mancuernas, registro, cart_detail, cart_add, cart_remove
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
    path('registro/', registro, name='registro'),
    path('cart/add/<int:mancuerna_id>/', cart_add, name='cart_add'),
    path('cart/remove/<int:mancuerna_id>/', cart_remove, name='cart_remove'),
    path('cart/', cart_detail, name='cart_detail'),
    path('direccion/', direccion_entrega, name='direccion_entrega'),
    path('pago/', pago, name='pago'),
    path('monedas/', monedas, name='monedas'),
    path('confirmacion/', confirmacion, name='confirmacion'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)