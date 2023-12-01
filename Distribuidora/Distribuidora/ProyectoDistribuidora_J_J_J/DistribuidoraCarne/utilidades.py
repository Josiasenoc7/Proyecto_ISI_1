from .models import ComprasDet, FacturaDet

def incrementar_stock_compra(compra):
    """
    Incrementa el stock de productos basado en una compra.
    """
    detalles_compra = ComprasDet.objects.filter(compra=compra)

    for detalle in detalles_compra:
        producto = detalle.producto
        cantidad = detalle.cantidad
        producto.stock += cantidad
        producto.save()

def decrementar_stock_venta(factura):
    """
    Decrementa el stock de productos basado en una venta.
    """
    detalles_venta = FacturaDet.objects.filter(factura=factura)

    for detalle in detalles_venta:
        producto = detalle.producto
        cantidad = detalle.cantidad
        producto.stock -= cantidad
        producto.save()
