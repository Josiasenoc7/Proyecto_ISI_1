from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Categoria, FacturaEnc, FacturaDet, ComprasDet, ComprasEnc,CAI, Pedido, Entrega, MetodoPago,  Clientes, Empleados, Producto, Proveedor, Sucursal, TipoCargo,TipoDocumento,Impuesto,HistorialCargo,Parametros_impuestos,PrecioHistorico
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

#Views de Empleados
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


#Views de Productos
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

#Views Proveedores
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


#Javier views Impuestos y Encabezado de factura

#Impuesto
class ImpuestoListView(ListView):
    model = Impuesto
    template_name = 'impuesto/impuesto_list.html'  # Ajusta el nombre de la plantilla según sea necesario
    context_object_name = 'impuestos'  # Nombre de la variable de contexto en la plantilla

class ImpuestoCreateView(CreateView):
    model = Impuesto
    template_name = 'impuesto/impuesto_form.html'  # Ajusta el nombre de la plantilla según sea necesario
    fields = ['nombre_impuesto','tipo_impuesto','valor_impuesto' ]  # Ajusta los campos según tu modelo
    success_url = reverse_lazy('impuesto-list')

class ImpuestoUpdateView(UpdateView):
    model = Impuesto
    template_name = 'impuesto/impuesto_form.html'  # Ajusta el nombre de la plantilla según sea necesario
    fields = ['nombre_impuesto','tipo_impuesto','valor_impuesto' ]  # Ajusta los campos según tu modelo
    success_url = reverse_lazy('impuesto-list')

class ImpuestoDeleteView(DeleteView):
    model = Impuesto
    template_name = 'impuesto/impuesto_confirm_delete.html'  # Ajusta el nombre de la plantilla según sea necesario
    success_url = reverse_lazy('impuesto-list')


# Vistas para HistorialCargo

class HistorialCargoListView(ListView):
    model = HistorialCargo
    template_name = 'historial_cargo_list.html'
    context_object_name = 'historial_cargos'

class HistorialCargoDetailView(DetailView):
    model = HistorialCargo
    template_name = 'historial_cargo_detail.html'
    context_object_name = 'historial_cargo'

class HistorialCargoCreateView(CreateView):
    model = HistorialCargo
    template_name = 'historial_cargo_form.html'
    fields = ['campo1', 'campo2']  # Reemplaza con los campos de tu modelo
    success_url = reverse_lazy('historial_cargo-list')

class HistorialCargoUpdateView(UpdateView):
    model = HistorialCargo
    template_name = 'historial_cargo_form.html'
    fields = ['campo1', 'campo2']  # Reemplaza con los campos de tu modelo
    success_url = reverse_lazy('historial_cargo-list')

class HistorialCargoDeleteView(DeleteView):
    model = HistorialCargo
    template_name = 'historial_cargo_confirm_delete.html'
    success_url = reverse_lazy('historial_cargo-list')


# Vistas para Parametros_impuestos

class ParametrosImpuestosListView(ListView):
    model = Parametros_impuestos
    template_name = 'parametros_impuestos_list.html'
    context_object_name = 'parametros_impuestos'

class ParametrosImpuestosDetailView(DetailView):
    model = Parametros_impuestos
    template_name = 'parametros_impuestos_detail.html'
    context_object_name = 'parametros_impuesto'

class ParametrosImpuestosCreateView(CreateView):
    model = Parametros_impuestos
    template_name = 'parametros_impuestos_form.html'
    fields = ['campo1', 'campo2']  # Reemplaza con los campos de tu modelo
    success_url = reverse_lazy('parametros_impuestos-list')

class ParametrosImpuestosUpdateView(UpdateView):
    model = Parametros_impuestos
    template_name = 'parametros_impuestos_form.html'
    fields = ['campo1', 'campo2']  # Reemplaza con los campos de tu modelo
    success_url = reverse_lazy('parametros_impuestos-list')

class ParametrosImpuestosDeleteView(DeleteView):
    model = Parametros_impuestos
    template_name = 'parametros_impuestos_confirm_delete.html'
    success_url = reverse_lazy('parametros_impuestos-list')


# Vistas para PrecioHistorico

class PrecioHistoricoListView(ListView):
    model = PrecioHistorico
    template_name = 'precio_historico_list.html'
    context_object_name = 'precios_historicos'

class PrecioHistoricoDetailView(DetailView):
    model = PrecioHistorico
    template_name = 'precio_historico_detail.html'
    context_object_name = 'precio_historico'

class PrecioHistoricoCreateView(CreateView):
    model = PrecioHistorico
    template_name = 'precio_historico_form.html'
    fields = ['campo1', 'campo2']  # Reemplaza con los campos de tu modelo
    success_url = reverse_lazy('precio_historico-list')

class PrecioHistoricoUpdateView(UpdateView):
    model = PrecioHistorico
    template_name = 'precio_historico_form.html'
    fields = ['campo1', 'campo2']  # Reemplaza con los campos de tu modelo
    success_url = reverse_lazy('precio_historico-list')

class PrecioHistoricoDeleteView(DeleteView):
    model = PrecioHistorico
    template_name = 'precio_historico_confirm_delete.html'
    success_url = reverse_lazy('precio_historico-list')







class CAIListView(ListView):
    model = CAI
    template_name = 'cai/cai_list.html'  # Reemplaza 'cai_list.html' con la plantilla que desees
    context_object_name = 'cais'  # Nombre de la variable de contexto en la plantilla

class CAICreateView(CreateView):
    model = CAI
    template_name = 'cai/cai_form.html'  # Reemplaza 'cai_form.html' con la plantilla que desees
    fields = ['rango_inicial_factura', 'rango_final_factura', 'fecha_emision', 'fecha_vencimiento', 'sucursal', 'tipo_comprobante', 'activo', 'usuario_creacion', 'fecha_creacion', 'usuario_modificacion', 'fecha_modificacion']
    success_url = reverse_lazy('cai-list')

class CAIUpdateView(UpdateView):
    model = CAI
    template_name = 'cai/cai_form.html'  # Reemplaza 'cai_form.html' con la plantilla que desees
    fields = ['rango_inicial_factura', 'rango_final_factura', 'fecha_emision', 'fecha_vencimiento', 'sucursal', 'tipo_comprobante', 'activo', 'usuario_creacion', 'fecha_creacion', 'usuario_modificacion', 'fecha_modificacion']
    success_url = reverse_lazy('cai-list')

class CAIDeleteView(DeleteView):
    model = CAI
    template_name = 'cai/cai_confirm_delete.html'  # Reemplaza 'cai_confirm_delete.html' con la plantilla que desees
    success_url = reverse_lazy('cai-list')



class PedidoListView(ListView):
    model = Pedido
    template_name = 'pedido_list.html'
    context_object_name = 'pedidos'

class PedidoDetailView(DetailView):
    model = Pedido
    template_name = 'pedido_detail.html'
    context_object_name = 'pedido'

class PedidoCreateView(CreateView):
    model = Pedido
    template_name = 'pedido_form.html'
    fields = ['fecha_pedido', 'total_pedido', 'cliente']
    success_url = reverse_lazy('pedido_list')

class PedidoUpdateView(UpdateView):
    model = Pedido
    template_name = 'pedido_form.html'
    fields = ['fecha_pedido', 'total_pedido', 'cliente']
    context_object_name = 'pedido'
    success_url = reverse_lazy('pedido_list')

class PedidoDeleteView(DeleteView):
    model = Pedido
    template_name = 'pedido_confirm_delete.html'
    context_object_name = 'pedido'
    success_url = reverse_lazy('pedido_list')


# Vistas para Entrega
class EntregaListView(ListView):
    model = Entrega
    template_name = 'entrega_list.html'
    context_object_name = 'entregas'

class EntregaDetailView(DetailView):
    model = Entrega
    template_name = 'entrega_detail.html'
    context_object_name = 'entrega'

class EntregaCreateView(CreateView):
    model = Entrega
    template_name = 'entrega_form.html'
    fields = ['id_cliente', 'id_pedido', 'id_empleado', 'id_producto', 'fecha_entrega', 'hora_entrega', 'direccion_entrega', 'estado_entrega', 'costo_entrega', 'factura']
    success_url = reverse_lazy('entrega_list')

class EntregaUpdateView(UpdateView):
    model = Entrega
    template_name = 'entrega_form.html'
    fields = ['id_cliente', 'id_pedido', 'id_empleado', 'id_producto', 'fecha_entrega', 'hora_entrega', 'direccion_entrega', 'estado_entrega', 'costo_entrega', 'factura']
    context_object_name = 'entrega'
    success_url = reverse_lazy('entrega_list')

class EntregaDeleteView(DeleteView):
    model = Entrega
    template_name = 'entrega_confirm_delete.html'
    context_object_name = 'entrega'
    success_url = reverse_lazy('entrega_list')

# Vistas para MetodoPago
class MetodoPagoListView(ListView):
    model = MetodoPago
    template_name = 'metodopago_list.html'
    context_object_name = 'metodospago'

class MetodoPagoDetailView(DetailView):
    model = MetodoPago
    template_name = 'metodopago_detail.html'
    context_object_name = 'metodopago'

class MetodoPagoCreateView(CreateView):
    model = MetodoPago
    template_name = 'metodopago_form.html'
    fields = ['id_cliente', 'tipo_metodo_pago', 'nombre_titular', 'numero_tarjeta', 'fecha_vencimiento', 'cvv']
    success_url = reverse_lazy('metodopago_list')

class MetodoPagoUpdateView(UpdateView):
    model = MetodoPago
    template_name = 'metodopago_form.html'
    fields = ['id_cliente', 'tipo_metodo_pago', 'nombre_titular', 'numero_tarjeta', 'fecha_vencimiento', 'cvv']
    context_object_name = 'metodopago'
    success_url = reverse_lazy('metodopago_list')

class MetodoPagoDeleteView(DeleteView):
    model = MetodoPago
    template_name = 'metodopago_confirm_delete.html'
    context_object_name = 'metodopago'
    success_url = reverse_lazy('metodopago_list')

class ComprasEncListView(ListView):
    model = ComprasEnc
    template_name = 'comprasenc_list.html'
    context_object_name = 'comprasenc'

class ComprasEncDetailView(DetailView):
    model = ComprasEnc
    template_name = 'comprasenc_detail.html'
    context_object_name = 'comprasenc'

class ComprasEncCreateView(CreateView):
    model = ComprasEnc
    template_name = 'comprasenc_form.html'
    fields = '__all__'
    success_url = '/'

class ComprasEncUpdateView(UpdateView):
    model = ComprasEnc
    template_name = 'comprasenc_form.html'
    fields = '__all__'
    context_object_name = 'comprasenc'
    success_url = '/'

class ComprasEncDeleteView(DeleteView):
    model = ComprasEnc
    template_name = 'comprasenc_confirm_delete.html'
    context_object_name = 'comprasenc'
    success_url = '/'

class ComprasDetListView(ListView):
    model = ComprasDet
    template_name = 'comprasdet_list.html'
    context_object_name = 'comprasdet'

class ComprasDetDetailView(DetailView):
    model = ComprasDet
    template_name = 'comprasdet_detail.html'
    context_object_name = 'comprasdet'

class ComprasDetCreateView(CreateView):
    model = ComprasDet
    template_name = 'comprasdet_form.html'
    fields = '__all__'
    success_url = '/'

class ComprasDetUpdateView(UpdateView):
    model = ComprasDet
    template_name = 'comprasdet_form.html'
    fields = '__all__'
    context_object_name = 'comprasdet'
    success_url = '/'

class ComprasDetDeleteView(DeleteView):
    model = ComprasDet
    template_name = 'comprasdet_confirm_delete.html'
    context_object_name = 'comprasdet'
    success_url = '/'

# Vistas para FacturaEnc
class FacturaEncListView(ListView):
    model = FacturaEnc
    template_name = 'facturaenc_list.html'
    context_object_name = 'facturaenc'

class FacturaEncDetailView(DetailView):
    model = FacturaEnc
    template_name = 'facturaenc_detail.html'
    context_object_name = 'facturaenc'

class FacturaEncCreateView(CreateView):
    model = FacturaEnc
    template_name = 'facturaenc_form.html'
    fields = '__all__'
    success_url = '/'

class FacturaEncUpdateView(UpdateView):
    model = FacturaEnc
    template_name = 'facturaenc_form.html'
    fields = '__all__'
    context_object_name = 'facturaenc'
    success_url = '/'

class FacturaEncDeleteView(DeleteView):
    model = FacturaEnc
    template_name = 'facturaenc_confirm_delete.html'
    context_object_name = 'facturaenc'
    success_url = '/'

# Vistas para FacturaDet
class FacturaDetListView(ListView):
    model = FacturaDet
    template_name = 'facturadet_list.html'
    context_object_name = 'facturadet'

class FacturaDetDetailView(DetailView):
    model = FacturaDet
    template_name = 'facturadet_detail.html'
    context_object_name = 'facturadet'

class FacturaDetCreateView(CreateView):
    model = FacturaDet
    template_name = 'facturadet_form.html'
    fields = '__all__'
    success_url = '/'

class FacturaDetUpdateView(UpdateView):
    model = FacturaDet
    template_name = 'facturadet_form.html'
    fields = '__all__'
    context_object_name = 'facturadet'
    success_url = '/'

class FacturaDetDeleteView(DeleteView):
    model = FacturaDet
    template_name = 'facturadet_confirm_delete.html'
    context_object_name = 'facturadet'
    success_url = '/'
