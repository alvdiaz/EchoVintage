from django.urls import path
from django.contrib.auth.decorators import user_passes_test
from .views import home, cassetes, carrito, cds, contacto, vinilos, agregarvinilo, modificar_producto, listar_productos, eliminar_producto, agregarcassette, agregarcd, login, registro

urlpatterns = [
    path('', home, name="home"),
    path('cassetes/', cassetes, name="cassetes"),
    path('carrito/', carrito, name="carrito"),
    path('cds/', cds, name="cds"),
    path('contacto/', contacto, name="contacto"),
    path('vinilos/', vinilos, name="vinilos"),
    path('agregar-vinilo/',user_passes_test(lambda u: u.is_superuser) (agregarvinilo), name="agregarvinilo"),
    path('agregar-cassette/',user_passes_test(lambda u: u.is_superuser) (agregarcassette), name="agregar_cassette"),
    path('agregar-cd/',user_passes_test(lambda u: u.is_superuser) (agregarcd), name="agregar_cd"),
    path('listar-productos/',user_passes_test(lambda u: u.is_superuser) (listar_productos), name="listar_productos"),
    path('modificar-producto/<str:tipo>/<id>/',user_passes_test(lambda u: u.is_superuser) (modificar_producto), name="modificar_producto"),
    path('eliminar-producto/<str:tipo>/<int:id>/',user_passes_test(lambda u: u.is_superuser)(eliminar_producto), name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    ]
