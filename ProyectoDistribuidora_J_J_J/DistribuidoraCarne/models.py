from django.db import models
# Asumiendo que las validaciones se encuentran correctamente definidas en el archivo 'validaciones.py'
from DistribuidoraCarne.validaciones import validar_nombre, validar_telefono, validar_correo, validar_date_time, validar_descripcion, validar_estado, validar_direccion, validar_rtn, validar_fecha_nacimiento, validar_nivel_maximo_stock, validar_nivel_minimo_stock, validar_salario, validar_fecha_actualizacion, validar_valor_impuesto

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50)

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
    nombre_surcusal = models.CharField(max_length=65, validators=[validar_nombre])
    ciudad = models.CharField(max_length=65, validators=[validar_nombre])
    direccion = models.CharField(max_length=255, validators=[validar_direccion])
    telefono = models.CharField(max_length=50, validators=[validar_telefono])

    def __str__(self):
        return self.nombre_surcusal

    class Meta:
        verbose_name = 'Surcusal'
        verbose_name_plural = 'Surcusales'

class TipoCargo(models.Model):
    nombre = models.CharField(max_length=50, validators=[validar_nombre])
    descripcion = models.CharField(max_length=200, validators=[validar_descripcion])
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateField(auto_now_add=True, validators=[validar_fecha_actualizacion])
    ultima_actualizacion = models.DateField(validators=[validar_fecha_actualizacion])
    descripcion_actualizacion = models.CharField(max_length=255, validators=[validar_descripcion])

    def __str__(self):
        return self.nombre

class Empleados(models.Model):
    id_empleado = models.CharField(max_length=15, default='0801199900123')
    nombre_empleado = models.CharField(max_length=65, validators=[validar_nombre])
    fecha_nacimiento = models.DateField(validators=[validar_fecha_nacimiento])
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE, default=1)
    correo = models.ForeignKey(Correo, on_delete=models.CASCADE, default=1)
    tipo_cargo = models.ForeignKey(TipoCargo, on_delete=models.CASCADE, default=1)
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, default=1)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre_empleado

class HistorialCargo(models.Model):
    nombre_empleado = models.ForeignKey(Empleados, on_delete=models.CASCADE)
    tipo_cargo = models.ForeignKey(TipoCargo, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre_empleado} - {self.tipo_cargo}"

class Clientes(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, default=1)
    documento = models.CharField(max_length=15, default='0801199900123')
    nombre_cliente = models.CharField(max_length=65, validators=[validar_nombre])
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE, default=1)
    correo = models.ForeignKey(Correo, on_delete=models.CASCADE, default=1)
    direccion = models.CharField(max_length=150, validators=[validar_direccion])

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
    telefono = models.CharField(max_length=8, validators=[validar_telefono])
    correo = models.CharField(max_length=65, null=True, validators=[validar_correo])
    direccion = models.CharField(max_length=255, validators=[validar_direccion])
    rtn = models.CharField(max_length=14, validators=[validar_rtn])
    celular_contacto = models.CharField(max_length=8, validators=[validar_telefono])
    fecha_registro = models.DateField(validators=[validar_date_time])

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre_proveedor

class Impuesto(models.Model):
    nombre_impuesto = models.CharField(max_length=20, validators=[validar_nombre])
    tipo_impuesto = models.CharField(max_length=50, validators=[validar_descripcion])
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
    nombre_producto = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, default=150)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2, default=200)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey('Categoria', on_delete=models.CASCADE, default=1)
    proveedor = models.ForeignKey('Proveedor', on_delete=models.CASCADE, default=1)
    impuesto = models.ForeignKey('Impuesto', on_delete=models.CASCADE, default=1)
    fecha_agregado = models.DateField(auto_now_add=True)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre_producto

class PrecioHistorico(models.Model):
    fecha_modificacion = models.DateTimeField(auto_now_add=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Precio Histórico'
        verbose_name_plural = 'Precios Históricos'
    class Meta:
        verbose_name = 'Precio Histórico'
        verbose_name_plural = 'Precios Históricos'



class Inventario(models.Model):
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, default=1)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    fecha_entrada = models.DateTimeField()
    cantidad = models.PositiveIntegerField()
    nivel_minimo_stock_inventario = models.DecimalField(max_digits=10, decimal_places=2)
    nivel_maximo_stock_inventario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.sucursal} - {self.producto}"

class Devoluciones(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=255, validators=[validar_descripcion])
    fecha_devolucion = models.DateField(validators=[validar_date_time])

    class Meta:
        verbose_name = 'Devolucion'
        verbose_name_plural = 'Devoluciones'

    def __str__(self):
        return self.descripcion

class Cotizacion(models.Model):
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_cotizacion = models.DateField(validators=[validar_date_time])
    total_cotizacion = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'

    def __str__(self):
        return str(self.id_cliente)

class EncabezadoFactura(models.Model):
    surcusal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.sucursal)

    class Meta:
        db_table = 'encabezado_factura'



