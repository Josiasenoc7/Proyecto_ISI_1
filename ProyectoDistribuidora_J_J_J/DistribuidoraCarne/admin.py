from django.contrib import admin
from .models import Categoria, Clientes, Empleados, Producto, Proveedor, Inventario,TipoCargo,TipoDocumento,Sucursal, Devoluciones, Cotizacion,Impuesto, EncabezadoFactura, PrecioHistorico, Parametros_impuestos, HistorialCargo

'''
@admin.register(TipoCargo)
class TipoCargoListView(admin.ModelAdmin):
    list_display = ('id','nombre', 'descripcion', 'salario_base','fecha_creacion','ultima_actualizacion','fecha_actualizacion')
    search_fields = ('id','nombre', 'descripcion', 'salario_base','fecha_creacion','ultima_actualizacion','fecha_actualizacion')
'''
@admin.register(Proveedor)
class ProveedorListView(admin.ModelAdmin):
    list_display = ('id','nombre_proveedor','direccion','rtn','nombre_contacto','celular_contacto','fecha_registro')
    search_fields = ('id','nombre_proveedor','telefono', 'correo', 'direccion','rtn','nombre_contacto','celular_contacto','fecha_registro')


@admin.register(Clientes)
class ClientesListView(admin.ModelAdmin):
    list_display = ('id','tipo_documento','documento','nombre_cliente','direccion','rtn')
    search_fields = ('id','tipo_documento','documento','nombre_cliente','telefono','correo','direccion','rtn')
   
'''
@admin.register(Categoria)
class CategoriaListView(admin.ModelAdmin):
    list_display = ('id', 'nombre_categoria','estado')
    search_fields = ('id', 'nombre_categoria','estado')
    
   
@admin.register(Empleados)
class EmpleadosListView(admin.ModelAdmin):
    list_display = ('id','nombre_empleado','fecha_nacimiento','salario','cargo')
    search_fields = ('id','nombre_empleado','fecha_nacimiento','salario', 'email', 'telefono', 'cargo')
    ordering = ('id','nombre_empleado')

@admin.register(Producto)
class ProductoListView(admin.ModelAdmin):
    list_display = ('id','nombre_producto','descripcion', 'precio','stock', 'fecha_agregado')
    search_fields = ('id','nombre_producto','descripcion', 'precio', 'stock', 'fecha_agregado')
    ordering = ('id','nombre_producto')

@admin.register(Impuesto)
class ImpuestoListView(admin.ModelAdmin):
     list_display = ('id','nombre_impuesto','descripcion', 'valor_impuesto')
     search_fields = ('id','nombre_impuesto','descripcion', 'valor_impuesto')
    
@admin.register(Parametros_impuestos)
class Parametros_impuestoListView(admin.ModelAdmin):
     list_display = ('id','fecha_inicial','fecha_final')
     search_fields = ('id','nombre_impuesto', 'valor_impuesto','fecha_inicial','fecha_final')

@admin.register(PrecioHistorico)
class PrecioHistoricoListView(admin.ModelAdmin):
     list_display = ('id','producto','fecha_inicio','fecha_final','fecha_modificacion','precio_anterior','descripcion_cambio')
     search_fields = ('id','producto','fecha_inicio','fecha_final','fecha_modificacion','precio_anterior','descripcion_cambio')
    
@admin.register(HistorialCargo)
class HistorialCargoListView(admin.ModelAdmin):
     list_display = ('id','nombre_empleado','fecha_inicio','fecha_fin')
     search_fields = ('id','nombre_empleado','fecha_inicio','fecha_fin')
'''

#admin.site.register(Clientes)
admin.site.register(Empleados)
admin.site.register(Producto)
#admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Inventario)
admin.site.register(TipoCargo)
admin.site.register(TipoDocumento)
admin.site.register(Sucursal)
admin.site.register(Devoluciones)
admin.site.register(Cotizacion)
admin.site.register(Impuesto)
admin.site.register(EncabezadoFactura)
admin.site.register(HistorialCargo)
admin.site.register(PrecioHistorico)
admin.site.register(Parametros_impuestos)


