from django.db import models
# Asumiendo que las validaciones se encuentran correctamente definidas en el archivo 'validaciones.py'
from DistribuidoraCarne.validaciones import  validar_Total_Cotizacion, validar_total_pedido, validar_nombre, validar_telefono, validar_correo, validar_date_time, validar_descripcion, validar_estado, validar_direccion, validar_rtn, validar_fecha_nacimiento, validar_nivel_maximo_stock, validar_nivel_minimo_stock, validar_stock ,validar_salario, validar_fecha_actualizacion, validar_valor_impuesto, validar_precio

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50, validators=[validar_nombre])

    def __str__(self):
        return self.nombre

class Correo(models.Model):
    correo = models.CharField(max_length=50, validators=[validar_correo])

    def __str__(self):
        return self.correo

class Telefono(models.Model):
    telefono = models.CharField(max_length=50, validators=[validar_telefono])

    def __str__(self):
        return self.telefono

class Sucursal(models.Model):
    nombre_sucursal = models.CharField(max_length=65, validators=[validar_nombre])
    ciudad = models.CharField(max_length=65, validators=[validar_nombre])
    direccion = models.CharField(max_length=255, validators=[validar_direccion])
    telefono = models.CharField(max_length=50, validators=[validar_telefono])
    rtn = models.CharField(max_length=14, validators=[validar_rtn])

    def __str__(self):
        return self.nombre_sucursal

    class Meta:
        verbose_name = 'Sucursal'
        verbose_name_plural = 'Sucursales'

class CAI(models.Model):
    rango_inicial_factura = models.IntegerField()
    rango_final_factura = models.IntegerField()
    fecha_emision = models.DateField()
    fecha_vencimiento = models.DateField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    tipo_comprobante = models.CharField(max_length=20)
    activo = models.BooleanField()

    def __str__(self):
        return str(self.rango_inicial_factura)

class TipoCargo(models.Model):
    nombre = models.CharField(max_length=50, validators=[validar_nombre])
    descripcion = models.CharField(max_length=200, validators=[validar_descripcion])
    salario_base = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_salario])
    fecha_creacion = models.DateField(auto_now_add=True, validators=[validar_fecha_actualizacion])
    ultima_actualizacion = models.DateField(validators=[validar_fecha_actualizacion])
    descripcion_actualizacion = models.CharField(max_length=255, validators=[validar_descripcion])

    def __str__(self):
        return self.nombre

class Empleados(models.Model):
    nombre_empleado = models.CharField(max_length=65, validators=[validar_nombre])
    fecha_nacimiento = models.DateField(validators=[validar_fecha_nacimiento])
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE, default=1)
    correo = models.ForeignKey(Correo, on_delete=models.CASCADE, default=1)
    tipo_cargo = models.ForeignKey(TipoCargo, on_delete=models.CASCADE, default=1)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, default=1)
    documento = models.CharField(max_length=15, default='0801199900123')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre_empleado

class HistorialCargo(models.Model):
    nombre_empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    fecha_inicio = models.DateField(validators=[validar_fecha_actualizacion])
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_empleado}"

class Clientes(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, default=1)
    documento = models.CharField(max_length=15, default='0801199900123')
    nombre_cliente = models.CharField(max_length=65, validators=[validar_nombre])
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE, default=1)
    correo = models.ForeignKey(Correo, on_delete=models.CASCADE, default=1)
    direccion = models.CharField(max_length=150, validators=[validar_direccion])
    rtn = models.CharField(max_length=14, validators=[validar_rtn])


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nombre_cliente

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=65, validators=[validar_nombre])
    estado = models.BooleanField(null=True, validators=[validar_estado])

    def __str__(self):
        return self.nombre_categoria

class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=65, validators=[validar_nombre])
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE, default=1)
    correo = models.CharField(max_length=65, null=True, validators=[validar_correo])
    direccion = models.CharField(max_length=255, validators=[validar_direccion])
    rtn = models.CharField(max_length=14, validators=[validar_rtn])
    nombre_contacto = models.CharField(max_length=50, validators=[validar_nombre])
    celular_contacto = models.CharField(max_length=50, validators=[validar_telefono])
    fecha_registro = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre_proveedor

class Impuesto(models.Model):
    nombre_impuesto = models.CharField(max_length=20, validators=[validar_nombre])
    descripcion = models.CharField(max_length=50, validators=[validar_descripcion])
    valor_impuesto = models.DecimalField(max_digits=5, decimal_places=2, default=00.00, validators=[validar_valor_impuesto])

    def __str__(self):
        return self.nombre_impuesto

    class Meta:
        db_table = 'impuesto'

class Parametros_impuestos(models.Model):
    id_impuesto = models.ForeignKey(Impuesto, on_delete=models.CASCADE, default=1)
    fecha_inicial = models.DateField(auto_now_add=True, validators=[validar_fecha_actualizacion])
    fecha_final = models.DateField(validators=[validar_fecha_actualizacion])

    def __str__(self):
        return str(self.id_impuesto)
    
    class Meta:
        verbose_name = 'Parametro impuesto'
        verbose_name_plural = 'Parametros impuestos'

class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50, validators=[validar_nombre])
    descripcion = models.CharField(max_length=255, validators=[validar_descripcion])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=150, validators=[validar_precio])
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, default=200, validators=[validar_precio])
    stock = models.PositiveIntegerField(validators=[validar_stock])
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, default=1)
    impuesto = models.ForeignKey('Impuesto', on_delete=models.CASCADE, default=1)
    fecha_agregado = models.DateField(auto_now_add=True)
    estado = models.BooleanField(validators=[validar_estado])

    def __str__(self):
        return self.nombre_producto
    
class Pedido(models.Model):
    id_clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField()
    total_pedido = models.FloatField(validators=[validar_total_pedido])
 

    def __str__(self):
        return str(self.fecha_pedido)

class PrecioHistorico(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    fecha_modificacion = models.DateField(auto_now_add=True)
    precio_anterior = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_precio])
    descripcion_cambio = models.CharField(max_length=255, validators=[validar_descripcion])
    

    class Meta:
        verbose_name = 'Precio Histórico'
        verbose_name_plural = 'Precios Históricos'
    
    def __str__(self):
        return f"{self.fecha_modificacion}" 
    
class Inventario(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, default=1)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    fecha_entrada = models.DateField(auto_now_add=True)
    cantidad = models.PositiveIntegerField(validators=[validar_stock])
    nivel_minimo_stock_inventario = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_nivel_minimo_stock])
    nivel_maximo_stock_inventario = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_nivel_maximo_stock])

    def __str__(self):
        return f"{self.sucursal} - {self.producto}"

class Devoluciones(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    cantidad = models.IntegerField(validators=[validar_stock])
    descripcion = models.CharField(max_length=255, validators=[validar_descripcion])
    fecha_devolucion = models.DateField(validators=[validar_fecha_actualizacion])

    class Meta:
        verbose_name = 'Devolucion'
        verbose_name_plural = 'Devoluciones'

    def __str__(self):
        return self.descripcion

class Cotizacion(models.Model):
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_cotizacion = models.DateField(validators=[validar_fecha_actualizacion])
   
    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'

    def __str__(self):
        return str(self.id_cliente)

class Entrega(models.Model):
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_entrega = models.DateField(null=True, blank=True)
    hora_entrega = models.TimeField(null=True, blank=True)
    direccion_entrega = models.CharField(max_length=255, null=True, blank=True, validators=[validar_direccion])
    estado_entrega = models.CharField(max_length=50, null=True, blank=True)
    costo_entrega = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, validators=[validar_Total_Cotizacion])
    # factura = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.direccion_entrega)
    
class MetodoPago(models.Model):
   
    tipo_metodo_pago = models.CharField(max_length=20, validators=[validar_nombre])
    
    def __str__(self):
        return str(self.tipo_metodo_pago)

class ComprasEnc(models.Model):
    fecha_compra=models.DateField(null=True,blank=True, validators=[validar_date_time])
    observacion=models.TextField(blank=True,null=True, validators=[validar_descripcion])
    no_factura=models.CharField(max_length=100)
    fecha_factura=models.DateField()
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0, validators=[validar_Total_Cotizacion])

    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    
    def _str_(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        if self.sub_total == None  or self.descuento == None:
            self.sub_total = 0
            self.descuento = 0
            
        self.total = self.sub_total - self.descuento
        super(ComprasEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Compras"
        verbose_name="Encabezado Compra"

class ComprasDet(models.Model):
    compra=models.ForeignKey(ComprasEnc,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)
    precio_prv=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)
    costo=models.FloatField(default=0)
    cos=models.AutoField
    def _str_(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio_prv))
        self.total = self.sub_total - float(self.descuento)
        super(ComprasDet, self).save()
    
    class Mega:
        verbose_name_plural = "Detalles Compras"
        verbose_name="Detalle Compra"

class FacturaEnc(models.Model):
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def _str_(self):
        return '{}'.format(self.id)

    def save(self):
        self.total = self.sub_total - self.descuento
        super(FacturaEnc,self).save()

    class Meta:
        verbose_name_plural = "Encabezado Facturas"
        verbose_name="Encabezado Factura"
  
class FacturaDet(models.Model):
    factura = models.ForeignKey(FacturaEnc,on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto,on_delete=models.CASCADE)
    cantidad=models.BigIntegerField(default=0)
    precio=models.FloatField(default=0)
    sub_total=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    total=models.FloatField(default=0)

    def _str_(self):
        return '{}'.format(self.producto)

    def save(self):
        self.sub_total = float(float(int(self.cantidad)) * float(self.precio))
        self.total = self.sub_total - float(self.descuento)
        super(FacturaDet, self).save()
    
    class Meta:
        verbose_name_plural = "Detalles Facturas"
        verbose_name="Detalle Factura"
