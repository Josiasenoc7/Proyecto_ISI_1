from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categoria, Clientes, Empleados, Producto, Proveedor, Sucursal, TipoCargo,TipoDocumento
from django.urls import reverse_lazy


    
# Vista basada en clase para listar los tipos de cargo
class TipoCargoListView(ListView):
    model = TipoCargo
    template_name = 'tipo_cargo_list.html'  # Reemplaza con la ruta de tu plantilla HTML
    context_object_name = 'tipos_cargo'  # Nombre de la variable en la plantilla


# Vista basada en clase para ver los detalles de un tipo de cargo
class TipoCargoDetailView(DetailView):
    model = TipoCargo
    template_name = 'tipo_cargo_detail.html'  # Reemplaza con la ruta de tu plantilla HTML
    context_object_name = 'tipo_cargo'  # Nombre de la variable en la plantilla
# Vista basada en clase para crear un nuevo tipo de cargo
class TipoCargoCreateView(CreateView):
    model = TipoCargo
    template_name = 'tipo_cargo_form.html'  # Reemplaza con la ruta de tu plantilla HTML
    fields = ['nombre']
    success_url = reverse_lazy('tipo_cargo_list')

# Vista basada en clase para actualizar un tipo de cargo existente
class TipoCargoUpdateView(UpdateView):
    model = TipoCargo
    template_name = 'tipo_cargo_form.html'  # Reemplaza con la ruta de tu plantilla HTML
    fields = ['nombre']
    context_object_name = 'tipo_cargo'  # Nombre de la variable en la plantilla

# Vista basada en clase para eliminar un tipo de cargo
class TipoCargoDeleteView(DeleteView):
    model = TipoCargo
    template_name = 'tipo_cargo_confirm_delete.html'  # Reemplaza con la ruta de tu plantilla HTML
    context_object_name = 'tipo_cargo'  # Nombre de la variable en la plantilla
    success_url = reverse_lazy('tipo-cargo-list')
    
    
    
    
    

# Vista basada en clase para listar las sucursales
class SucursalListView(ListView):
    model = Sucursal
    template_name = 'sucursal/sucursal_list.html'  # Reemplaza con la ruta de tu plantilla HTML
    context_object_name = 'sucursales'  # Nombre de la variable en la plantilla

# Vista basada en clase para ver los detalles de una sucursal
class SucursalDetailView(DetailView):
    model = Sucursal
    template_name = 'sucursal/sucursal_detail.html'  # Reemplaza con la ruta de tu plantilla HTML
    context_object_name = 'sucursal'  # Nombre de la variable en la plantilla

# Vista basada en clase para crear una nueva sucursal
class SucursalCreateView(CreateView):
    model = Sucursal
    template_name = 'sucursal/sucursal_form.html'  # Reemplaza con la ruta de tu plantilla HTML
    fields = ['nombre_surcusal', 'ciudad', 'direccion', 'telefono']

# Vista basada en clase para actualizar una sucursal existente
class SucursalUpdateView(UpdateView):
    model = Sucursal
    template_name = 'sucursal/sucursal_form.html'  # Reemplaza con la ruta de tu plantilla HTML
    fields = ['nombre_surcusal', 'ciudad', 'direccion', 'telefono']
    context_object_name = 'sucursal'  # Nombre de la variable en la plantilla

# Vista basada en clase para eliminar una sucursal
class SucursalDeleteView(DeleteView):
    model = Sucursal
    template_name = 'sucursal/sucursal_confirm_delete.html'  # Reemplaza con la ruta de tu plantilla HTML
    context_object_name = 'sucursal'  # Nombre de la variable en la plantilla

# Vista basada en clase para listar los registros de TipoDocumento
class TipoDocumentoListView(ListView):
    model = TipoDocumento
    template_name = 'tipo_documento_list.html'
    context_object_name = 'tipo_documentos'

# Vista basada en clase para crear un nuevo registro de TipoDocumento
class TipoDocumentoCreateView(CreateView):
    model = TipoDocumento
    template_name = 'tipo_documento_form.html'
    fields = ['nombre']

# Vista basada en clase para actualizar un registro de TipoDocumento
class TipoDocumentoUpdateView(UpdateView):
    model = TipoDocumento
    template_name = 'tipo_documento_form.html'
    fields = ['nombre']

# Vista basada en clase para eliminar un registro de TipoDocumento
class TipoDocumentoDeleteView(DeleteView):
    model = TipoDocumento
    template_name = 'tipo_documento_confirm_delete.html'





# Vista basada en clase para listar categorías
class CategoriaListView(ListView):
    model = Categoria
    template_name = 'categoria_list.html'
    context_object_name = 'categorias'


# Vista basada en clase para ver detalles de una categoría
class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'categoria_detail.html'
    context_object_name = 'categoria'

# Vista basada en clase para crear una nueva categoría
class CategoriaCreateView(CreateView):
    model = Categoria
    template_name = 'categoria_form.html'
    fields = ['nombre_categoria', 'descripcion', 'estado', 'nivel_actual_stock', 'nivel_maximo_stock', 'nivel_minimo_stock', 'creacion_categoria']

# Vista basada en clase para actualizar una categoría existente
class CategoriaUpdateView(UpdateView):
    model = Categoria
    template_name = 'categoria_form.html'
    fields = ['nombre_categoria', 'descripcion', 'estado', 'nivel_actual_stock', 'nivel_maximo_stock', 'nivel_minimo_stock', 'creacion_categoria']

# Vista basada en clase para eliminar una categoría
class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'categoria_confirm_delete.html'
    success_url = '/categorias/'  # Redirige a la lista de categorías
    
    
    
    

# Repite un patrón similar para los otros modelos (Clientes, Empleados, Producto, Proveedor).

class ClientesListView(ListView):
    model = Clientes
    template_name = 'clientes_list.html'
    context_object_name = 'clientes'
    fields = ['nombre_cliente', 'telefono', 'correo', 'direccion']

# Vista basada en clase para ver detalles de un cliente
class ClientesDetailView(DetailView):
    model = Clientes
    template_name = 'clientes_detail.html'
    context_object_name = 'cliente'

# Vista basada en clase para crear un nuevo cliente
class ClientesCreateView(CreateView):
    model = Clientes
    template_name = 'clientes_form.html'
    fields = ['nombre_cliente', 'telefono', 'correo', 'direccion']

# Vista basada en clase para actualizar un cliente existente
class ClientesUpdateView(UpdateView):
    model = Clientes
    template_name = 'clientes_form.html'
    fields = ['nombre_cliente', 'telefono', 'correo', 'direccion']

# Vista basada en clase para eliminar un cliente
class ClientesDeleteView(DeleteView):
    model = Clientes
    template_name = 'clientes_confirm_delete.html'
    success_url = '/clientes/'  # Redirige a la lista de clientes



class EmpleadosListView(ListView):
    model = Empleados
    template_name = 'empleados/empleados_list.html'  # Reemplaza 'empleados_list.html' con la plantilla que desees
    context_object_name = 'empleados'  # Nombre de la variable de contexto en la plantilla

class EmpleadosCreateView(CreateView):
    model = Empleados
    template_name = 'empleados/empleados_form.html'  # Reemplaza 'empleados_form.html' con la plantilla que desees
    fields = ['nombre_empleado', 'fecha_nacimiento', 'salario', 'email', 'telefono', 'direccion', 'cargo']
    success_url = reverse_lazy('empleados-list')

class EmpleadosUpdateView(UpdateView):
    model = Empleados
    template_name = 'empleados/empleados_form.html'  # Reemplaza 'empleados_form.html' con la plantilla que desees
    fields = ['nombre_empleado', 'fecha_nacimiento', 'salario', 'email', 'telefono', 'direccion', 'cargo']
    success_url = reverse_lazy('empleados-list')

class EmpleadosDeleteView(DeleteView):
    model = Empleados
    template_name = 'empleados/empleados_confirm_delete.html'  # Reemplaza 'empleados_confirm_delete.html' con la plantilla que desees
    success_url = reverse_lazy('empleados-list')




class ProductoListView(ListView):
    model = Producto
    template_name = 'producto/producto_list.html'  # Reemplaza 'producto_list.html' con la plantilla que desees
    context_object_name = 'productos'  # Nombre de la variable de contexto en la plantilla

class ProductoCreateView(CreateView):
    model = Producto
    template_name = 'producto/producto_form.html'  # Reemplaza 'producto_form.html' con la plantilla que desees
    fields = ['nombre_producto', 'descripcion', 'precioventa', 'estado', 'stock', 'fecha_agregado']
    success_url = reverse_lazy('producto-list')

class ProductoUpdateView(UpdateView):
    model = Producto
    template_name = 'producto/producto_form.html'  # Reemplaza 'producto_form.html' con la plantilla que desees
    fields = ['nombre_producto', 'descripcion', 'precioventa', 'estado', 'stock', 'fecha_agregado']
    success_url = reverse_lazy('producto-list')

class ProductoDeleteView(DeleteView):
    model = Producto
    template_name = 'producto/producto_confirm_delete.html'  # Reemplaza 'producto_confirm_delete.html' con la plantilla que desees
    success_url = reverse_lazy('producto-list')





class ProveedorListView(ListView):
    model = Proveedor
    template_name = 'proveedor/proveedor_list.html'  # Reemplaza 'proveedor_list.html' con la plantilla que desees
    context_object_name = 'proveedores'  # Nombre de la variable de contexto en la plantilla

class ProveedorCreateView(CreateView):
    model = Proveedor
    template_name = 'proveedor/proveedor_form.html'  # Reemplaza 'proveedor_form.html' con la plantilla que desees
    fields = ['nombre_proveedor', 'contacto', 'telefono', 'correo', 'direccion', 'rtn', 'fecha_registro']
    success_url = reverse_lazy('proveedor-list')

class ProveedorUpdateView(UpdateView):
    model = Proveedor
    template_name = 'proveedor/proveedor_form.html'  # Reemplaza 'proveedor_form.html' con la plantilla que desees
    fields = ['nombre_proveedor', 'contacto', 'telefono', 'correo', 'direccion', 'rtn', 'fecha_registro']
    success_url = reverse_lazy('proveedor-list')

class ProveedorDeleteView(DeleteView):
    model = Proveedor
    template_name = 'proveedor/proveedor_confirm_delete.html'  # Reemplaza 'proveedor_confirm_delete.html' con la plantilla que desees
    success_url = reverse_lazy('proveedor-list')



# class CAIListView(ListView):
#     model = CAI
#     template_name = 'cai/cai_list.html'  # Reemplaza 'cai_list.html' con la plantilla que desees
#     context_object_name = 'cais'  # Nombre de la variable de contexto en la plantilla

# class CAICreateView(CreateView):
#     model = CAI
#     template_name = 'cai/cai_form.html'  # Reemplaza 'cai_form.html' con la plantilla que desees
#     fields = ['rango_inicial_factura', 'rango_final_factura', 'fecha_emision', 'fecha_vencimiento', 'sucursal', 'tipo_comprobante', 'activo', 'usuario_creacion', 'fecha_creacion', 'usuario_modificacion', 'fecha_modificacion']
#     success_url = reverse_lazy('cai-list')

# class CAIUpdateView(UpdateView):
#     model = CAI
#     template_name = 'cai/cai_form.html'  # Reemplaza 'cai_form.html' con la plantilla que desees
#     fields = ['rango_inicial_factura', 'rango_final_factura', 'fecha_emision', 'fecha_vencimiento', 'sucursal', 'tipo_comprobante', 'activo', 'usuario_creacion', 'fecha_creacion', 'usuario_modificacion', 'fecha_modificacion']
#     success_url = reverse_lazy('cai-list')

# class CAIDeleteView(DeleteView):
#     model = CAI
#     template_name = 'cai/cai_confirm_delete.html'  # Reemplaza 'cai_confirm_delete.html' con la plantilla que desees
#     success_url = reverse_lazy('cai-list')


