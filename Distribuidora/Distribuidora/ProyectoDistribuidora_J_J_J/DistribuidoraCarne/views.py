from django.shortcuts import render
from .models import ComprasEnc, ComprasDet
from .utils import incrementar_stock_compra

# Supongamos que tienes una vista para procesar una compra
def procesar_compra(request):
    # Lógica para procesar la compra y obtener los detalles
    nueva_compra = ComprasEnc.objects.create(...)
    nuevo_detalle_compra = ComprasDet.objects.create(compra=nueva_compra, producto=mi_producto, cantidad=mi_cantidad, ...)
    
    # Llamada a la función para incrementar el stock
    incrementar_stock_compra(nueva_compra)
    
    # Resto de la lógica de la vista...
