from django.db import models
from DistribuidoraCarne.validaciones import validar_nombre,validar_telefono,validar_correo,validar_date_time,validar_descripcion,validar_estado,validar_direccion
from DistribuidoraCarne.validaciones import validar_rtn,validar_fecha_nacimiento,validar_nivel_maximo_stock,validar_nivel_minimo_stock
from DistribuidoraCarne.validaciones import validar_date_time, validar_salario, validar_fecha_actualizacion, validar_salario_base, validar_id, validar_stock_actual,validar_Cantidad
from DistribuidoraCarne.validaciones import validar_Total_Cotizacion,validar_numero_tarjeta,validar_fecha_vencimiento,validar_cvv,validar_valor_impuesto,validar_nombre_titular,validar_nombre_negocio

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50, default='Identidad')
    def __str__(self):
        return self.nombre
    
class TipoCargo(models.Model):
    nombre = models.CharField(max_length=50, validators=[validar_nombre])
    descripcion = models.CharField(max_length=200, validators=[validar_descripcion])
    salario_base = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_salario_base])
    fecha_creacion = models.DateField(auto_now_add=True, validators=[validar_fecha_actualizacion])
    ultima_actualizacion = models.DateField(validators=[validar_fecha_actualizacion])
    descripcion_actualizacion = models.CharField(max_length=255, validators=[validar_descripcion])
    
    def __str__(self):
        return self.nombre
    
class Sucursal(models.Model):
    nombre_surcusal = models.CharField(max_length=65, validators=[validar_nombre])
    ciudad = models.CharField(max_length=65, validators=[validar_nombre])
    direccion = models.CharField(max_length=255, validators=[validar_direccion])
    telefono = models.CharField(max_length=50, validators=[validar_telefono])

    def __str__(self):
        return self.nombre_surcusal
    
    class Meta:
        verbose_name = 'Surcusal'
        verbose_name_plural = 'Surcusales'  
    
class Clientes(models.Model):
    id_cliente = models.CharField(max_length=15, validators=[validar_id])  # Campo para el número de identificación
    nombre_cliente = models.CharField(max_length=65,validators=[validar_nombre])
    telefono = models.CharField(max_length=20, validators=[validar_telefono])
    rtn = models.CharField(max_length=14, validators=[validar_rtn])
    correo = models.CharField(max_length=50, validators=[validar_correo])
    direccion = models.CharField(max_length=150, validators=[validar_direccion])
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
        def __str__(self):
            return self.nombre_cliente
    
class Empleados(models.Model):
    id_empleado = models.CharField(max_length=15, validators= [validar_id])# Campo para el número de identificación
    nombre_empleado = models.CharField(max_length=65 ,validators=[validar_nombre])
    fecha_nacimiento = models.DateField(validators=[validar_fecha_nacimiento])
    salario = models.DecimalField(max_digits=10, decimal_places=2,validators=[validar_salario])
    email = models.CharField(max_length=50, validators=[validar_correo])
    telefono = models.CharField(max_length=50, validators=[validar_telefono])
    direccion = models.CharField(max_length=255, validators=[validar_direccion])
    tipo_cargo = models.ForeignKey(TipoCargo, on_delete=models.CASCADE,default=1)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE,default=1)
    surcusal = models.ForeignKey(Sucursal, on_delete=models.CASCADE,default=1)


    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre_empleado    
  
class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=65, validators=[validar_nombre])
    stock_actual = models.CharField(max_length=4, validators=[validar_stock_actual])
    estado  = models.BooleanField(null=True, validators=[validar_estado])

    def __str__(self):
        return self.nombre_categoria        

class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=65, validators=[validar_nombre])
    telefono = models.CharField(max_length=8, validators=[validar_telefono])
    correo = models.CharField(max_length=65, null=True,validators=[validar_correo])
    direccion = models.CharField(max_length=255, validators=[validar_direccion])
    rtn = models.CharField(max_length=14,validators=[validar_rtn])
    nombre_proveedor = models.CharField(max_length=65, validators=[validar_nombre])
    celular_contacto = models.CharField(max_length=8,validators=[validar_telefono])
    fecha_registro = models.DateField(auto_now_add=True, validators=[validar_date_time])

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre_proveedor
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50, validators=[validar_nombre])
    descripcion = models.CharField(max_length=255,validators=[validar_descripcion])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2,default=150, validators=[validar_salario])
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2,default=200, validators=[validar_salario])
    stock = models.PositiveIntegerField(validators=[validar_stock_actual])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,default=1)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE,default=1)
    fecha_agregado = models.DateField(validators=[validar_date_time])
    estado = models.BooleanField(validators=[validar_estado])

    def __str__(self):
        return self.nombre_producto
    
class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=65, default='Inventario',validators=[validar_nombre])
    fecha_entrada = models.DateTimeField(validators=[validar_date_time])
    fecha_vencimiento = models.DateField()
    cantidad = models.PositiveIntegerField(validators=[validar_Cantidad]) 
    nivel_minimo_stock_inventario = models.DecimalField(max_digits=10, decimal_places=2)
    nivel_maximo_stock_inventario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre

class Devoluciones(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE,default=1)
    cantidad = models.IntegerField(validators=[validar_Cantidad])
    descripcion = models.CharField(max_length=255,validators=[validar_descripcion])
    fecha_devolucion = models.DateField(validators=[validar_date_time])


    class Meta:
        verbose_name = 'Devolucion'
        verbose_name_plural = 'Devoluciones'  

    def _str_(self):
        return self.descripcion

class Cotizacion(models.Model):
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_cotizacion = models.DateField(max_length=12, validators=[validar_date_time])
    total_cotizacion = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_Total_Cotizacion])
   

    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'  
    

    def _str_(self):
        return self.id_cliente

# Aqui trabajo Javier y se estan agregando los models de mpuesto, metodo de pago y encabezado de factura
class Impuesto(models.Model):
    id_impuesto = models.AutoField(primary_key=True)
    nombre_impuesto = models.CharField(max_length=20,validators=[validar_nombre])
    tipo_impuesto = models.CharField(max_length=50,validators=[validar_descripcion])
    valor_impuesto = models.DecimalField(max_digits=5, decimal_places=2,default=00.00, validators=[validar_valor_impuesto])

    def __str__(self):
        return f"{self.tipo_impuesto} - {self.nombre_impuesto}"

    class Meta:
        db_table = 'impuesto'
    
class MetodoPago(models.Model):
    DEBITO = 'debito'
    CREDITO = 'credito'

    TIPO_METODO_CHOICES = [
        (DEBITO, 'Débito'),
        (CREDITO, 'Crédito'),
    ]

    id_metodo_pago = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    tipo_metodo_pago = models.CharField(max_length=50, choices=TIPO_METODO_CHOICES, validators=[validar_descripcion])
    numero_tarjeta = models.CharField(max_length=25, validators=[validar_numero_tarjeta])
    fecha_vencimiento = models.DateField(validators=[validar_fecha_vencimiento])
    cvv = models.CharField(max_length=4, validators=[validar_cvv])
    nombre_titular = models.CharField(max_length=60, validators=[validar_nombre_titular])

    def __str__(self):
        return f"{self.get_tipo_metodo_pago_display()}"

    class Meta:
        db_table = 'metodo_pago'

class EncabezadoFactura(models.Model):
    id_encabezado = models.AutoField(primary_key=True)
    nombre_negocio = models.CharField(max_length=200, validators=[validar_nombre_negocio])
    direccion_negocio = models.CharField(max_length=200, validators=[validar_direccion])
    correo = models.CharField(max_length=100, null=True, validators=[validar_correo])
    rtn = models.CharField(max_length=20, validators=[validar_rtn])
    telefono = models.CharField(max_length=20, null=True, validators=[validar_telefono])

    def __str__(self):
        return f"{self.nombre_negocio} - {self.rtn}"

    class Meta:
        db_table = 'encabezado_factura'

