from django.contrib import admin
from .models import Categoria, Clientes, Empleados, Producto, Proveedor, Inventario,TipoCargo,TipoDocumento,Sucursal, Devoluciones, Cotizacion

@admin.register(TipoCargo)
class TipoCargoListView(admin.ModelAdmin):
    list_display = ('id','nombre')
    search_fields = ('id','nombre')
@admin.register(Proveedor)
class ProveedorListView(admin.ModelAdmin):
    list_display = ('id','nombre_proveedor','telefono', 'correo', 'direccion','rtn', 'fecha_registro')
    search_fields = ('id','nombre_proveedor','telefono', 'correo', 'direccion','rtn', 'fecha_registro')

'''
@admin.register(Clientes)
class ClientesListView(admin.ModelAdmin):
    list_display = ('id','nombre_cliente','telefono','correo', 'direccion')
    search_fields = ('id','nombre_cliente','telefono','correo', 'direccion')
    ordering = ('id','nombre_cliente')

@admin.register(Categoria)
class CategoriaListView(admin.ModelAdmin):
    list_display = ('id', 'nombre_categoria', 'descripcion_categoria', 'estado', 'nivel_actual_stock','nivel_maximo_stock', 'nivel_minimo_stock', 'creacion_categoria')
    search_fields = ('id', 'nombre_categoria', 'descripcion_categoria', 'estado', 'nivel_actual_stock','nivel_maximo_stock', 'nivel_minimo_stock', 'creacion_categoria')
    ordering = ('id','nombre_categoria')

@admin.register(Empleados)
class EmpleadosListView(admin.ModelAdmin):
    list_display = ('id','nombre_empleado','fecha_nacimiento','salario', 'email', 'telefono', 'cargo')
    search_fields = ('id','nombre_empleado','fecha_nacimiento','salario', 'email', 'telefono', 'cargo')
    ordering = ('id','nombre_empleado')

@admin.register(Producto)
class ProductoListView(admin.ModelAdmin):
    list_display = ('id','nombre_producto','descripcion', 'precioventa', 'stock', 'fecha_agregado')
    search_fields = ('id','nombre_producto','descripcion', 'precioventa', 'stock', 'fecha_agregado')
    ordering = ('id','nombre_producto')
@admin.register(Proveedor)
class ProveedorListView(admin.ModelAdmin):
    list_display = ('id','nombre_proveedor','telefono', 'correo', 'direccion','rtn', 'fecha_registro')
    search_fields = ('id','nombre_proveedor','telefono', 'correo', 'direccion','rtn', 'fecha_registro')
    ordering = ('id','nombre_proveedor')
    
    '''
 
admin.site.register(Clientes)
admin.site.register(Empleados)
admin.site.register(Producto)
#admin.site.register(Proveedor)
admin.site.register(Categoria)
admin.site.register(Inventario)
#admin.site.register(TipoCargo)
admin.site.register(TipoDocumento)
admin.site.register(Sucursal)
admin.site.register(Devoluciones)
admin.site.register(Cotizacion)


