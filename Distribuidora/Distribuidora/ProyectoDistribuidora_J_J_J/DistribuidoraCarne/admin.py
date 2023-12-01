from django.contrib import admin
from .models import TipoDocumento, TipoCargo, Correo, Telefono, Clientes, Categoria, Proveedor, Descuento, Impuesto, Producto, Inventario, Sucursal, Empleados, ComprasEncabezado, ComprasDetalle, ParametroSar, FacturaEncabezado, FacturaDet, Rutas, Transporte, Entrega, Devoluciones, Cotizacion, MetodoPago, Pedido

# Register your models here.
admin.site.register(TipoDocumento)
admin.site.register(TipoCargo)
admin.site.register(Correo)
admin.site.register(Telefono)
admin.site.register(Clientes)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Descuento)
admin.site.register(Impuesto)
admin.site.register(Producto)
admin.site.register(Inventario)
admin.site.register(Sucursal)
admin.site.register(Empleados)
admin.site.register(ComprasEncabezado)
admin.site.register(ComprasDetalle)
admin.site.register(ParametroSar)
admin.site.register(FacturaEncabezado)
admin.site.register(FacturaDet)
admin.site.register(Rutas)
admin.site.register(Transporte)
admin.site.register(Entrega)
admin.site.register(Devoluciones)
admin.site.register(Cotizacion)
admin.site.register(MetodoPago)
admin.site.register(Pedido)
