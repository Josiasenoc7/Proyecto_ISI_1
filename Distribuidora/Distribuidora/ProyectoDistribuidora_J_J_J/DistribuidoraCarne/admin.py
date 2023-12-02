from django.contrib import admin
from .models import TipoDocumento, TipoCargo, Correo, Telefono, Clientes, Categoria, Proveedor, Descuento, Impuesto, Producto, Inventario, Sucursal, Empleados, ComprasEncabezado, ComprasDetalle, ParametroSar, FacturaEncabezado, FacturaDet, Rutas, Transporte, Entrega, Devoluciones, Cotizacion, MetodoPago, Pedido


@admin.register(Clientes)
class ClientesAdmin(admin.ModelAdmin):
    list_display = ('id','nombre_cliente', 'apellido_cliente', 'tipo_documento', 'documento', 'telefono', 'correo', 'rtn', 'direccion')
    search_fields = ['nombre_cliente', 'apellido_cliente', 'documento', 'telefono', 'correo', 'rtn', 'direccion']

@admin.register(TipoDocumento)
class TipoDocumentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', )
    search_fields = ('id' , 'nombre',)
@admin.register(TipoCargo)
class TipoCargoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', )
    search_fields = ('id', 'nombre',)

@admin.register(Correo)
class CorreoAdmin(admin.ModelAdmin):
    list_display = ('id', 'correo', )
    search_fields = ('id', 'correo',)

@admin.register(Telefono)
class TelefonoAdmin(admin.ModelAdmin):
    list_display = ('id', 'telefono', )
    search_fields = ('id', 'telefono',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_categoria', 'estado')
    search_fields = ('id', 'nombre_categoria', 'estado')
@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_proveedor', 'telefono', 'correo', 'direccion', 'rtn', 'nombre_contacto', 'celular_contacto')
    search_fields = ('id', 'nombre_proveedor', 'telefono', 'correo', 'direccion', 'rtn', 'nombre_contacto', 'celular_contacto')

@admin.register(Descuento)
class DescuentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_descuento', 'descripción', 'valor_descuento', 'fecha_creación')
    search_fields = ('id', 'nombre_descuento', 'descripción', 'valor_descuento', 'fecha_creación')

@admin.register(Impuesto)
class ImpuestoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_impuesto', 'descripción', 'valor_impuesto', 'fecha_creación')
    search_fields = ('id', 'nombre_impuesto', 'descripción', 'valor_impuesto', 'fecha_creación')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_producto', 'descripcion', 'precio_venta', 'stock', 'categoria', 'proveedor', 'estado', 'fecha_creacion')
    search_fields = ('id', 'nombre_producto', 'descripcion', 'precio_venta', 'stock', 'categoria', 'proveedor', 'estado', 'fecha_creacion')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'producto', 'fecha_vencimiento', 'cantidad', 'Stock_minimo', 'Stock_maximo')
    search_fields = ('id', 'producto', 'fecha_vencimiento', 'cantidad', 'Stock_minimo', 'Stock_maximo')

@admin.register(Sucursal)
class SucursalAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_sucursal', 'ciudad', 'direccion', 'telefono', 'rtn', 'fecha_creacion')
    search_fields = ('id', 'nombre_sucursal', 'ciudad', 'direccion', 'telefono', 'rtn', 'fecha_creacion')

@admin.register(Empleados)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_documento', 'documento', 'nombre_empleado', 'apellido_empleado', 'fecha_nacimiento', 'telefono', 'correo', 'tipo_cargo', 'sucursal', 'fecha_creacion')
    search_fields = ('id', 'tipo_documento', 'documento', 'nombre_empleado', 'apellido_empleado', 'fecha_nacimiento', 'telefono', 'correo', 'tipo_cargo', 'sucursal', 'fecha_creacion')

@admin.register(ComprasEncabezado)
class ComprasEncabezadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'proveedor', 'no_factura', 'fecha_compra', 'observacion')
    search_fields = ('id', 'proveedor', 'no_factura', 'fecha_compra', 'observacion')

@admin.register(ComprasDetalle)
class ComprasDetalleAdmin(admin.ModelAdmin):
    list_display = ('id', 'compra', 'producto', 'cantidad', 'precio_compra', 'sub_total', 'descuento', 'total')
    search_fields = ('id', 'compra', 'producto', 'cantidad', 'precio_compra', 'sub_total', 'descuento', 'total')
@admin.register(ParametroSar)
class ParametroSarAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_inicio', 'numero_fin')
    search_fields = ('id', 'numero_inicio', 'numero_fin')

@admin.register(FacturaEncabezado)
class FacturaEncabezadoAdmin(admin.ModelAdmin):
    list_display = ('id', 'Empresa', 'fecha_emision', 'cai', 'fecha_creacion')
    search_fields = ('id', 'Empresa', 'fecha_emision', 'cai', 'fecha_creacion')

@admin.register(FacturaDet)
class FacturaDetAdmin(admin.ModelAdmin):
    list_display = ('id', 'factura', 'producto', 'cantidad', 'sub_total', 'descuento', 'impuesto', 'total')
    search_fields = ('id', 'factura', 'producto', 'cantidad', 'sub_total', 'descuento', 'impuesto', 'total')

@admin.register(Rutas)
class RutasAdmin(admin.ModelAdmin):
    list_display = ('id', 'ruta',)
    search_fields = ('id', 'ruta',)

@admin.register(Transporte)
class TransporteAdmin(admin.ModelAdmin):
    list_display = ('id', 'ruta', 'nombre_carro', 'codigo', 'chofer')
    search_fields = ('id', 'ruta', 'nombre_carro', 'codigo', 'chofer')

@admin.register(Entrega)
class EntregaAdmin(admin.ModelAdmin):
    list_display = ('id', 'carro', 'fecha_entrega', 'hora_entrega', 'direccion_entrega')
    search_fields = ('id', 'carro', 'fecha_entrega', 'hora_entrega', 'direccion_entrega')

@admin.register(Devoluciones)
class DevolucionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_producto', 'cantidad', 'descripcion', 'fecha_devolucion')
    search_fields = ('id', 'id_producto', 'cantidad', 'descripcion', 'fecha_devolucion')

@admin.register(Cotizacion)
class CotizacionAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_cliente', 'id_producto', 'fecha_cotizacion')
    search_fields = ('id', 'id_cliente', 'id_producto', 'fecha_cotizacion')

@admin.register(MetodoPago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'tipo_metodo_pago',)
    search_fields = ('id', 'tipo_metodo_pago',)

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_clientes', 'id_producto', 'fecha_pedido', 'total_pedido')
    search_fields = ('id', 'id_clientes', 'id_producto', 'fecha_pedido', 'total_pedido')
