from django.db import models
from DistribuidoraCarne.validaciones import validar_nombre,validar_telefono,validar_correo,validar_date_time,validar_descripcion,validar_estado,validar_direccion
from DistribuidoraCarne.validaciones import validar_rtn,validar_fecha_nacimiento,validar_nivel_maximo_stock,validar_nivel_minimo_stock
from DistribuidoraCarne.validaciones import validar_date_time, validar_salario

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50, default='Identidad')
    def __str__(self):
        return self.nombre
    
class TipoCargo(models.Model):
    nombre = models.CharField(max_length=50,default='Empleado')
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
    id_cliente = models.CharField(max_length=15, default='0801199900123')  # Campo para el número de identificación
    nombre_cliente = models.CharField(max_length=65,validators=[validar_nombre])
    telefono = models.CharField(max_length=20, validators=[validar_telefono])
    correo = models.CharField(max_length=50, validators=[validar_correo])
    direccion = models.CharField(max_length=150, validators=[validar_direccion])
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

def __str__(self):
     return self.nombre_cliente
    


class Empleados(models.Model):
    id_empleado = models.CharField(max_length=15, default='0801199900123')  # Campo para el número de identificación
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
    fecha_registro = models.DateField(validators=[validar_date_time])

    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre_proveedor
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50, validators=[validar_nombre])
    descripcion = models.CharField(max_length=255,validators=[validar_descripcion])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2,default=150)
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2,default=200)
    stock = models.PositiveIntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,default=1)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE,default=1)
    fecha_agregado = models.DateField(validators=[validar_date_time])
    estado = models.BooleanField(validators=[validar_estado])

    def __str__(self):
        return self.nombre_producto
    

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=65, default='Inventario')
    fecha_entrada = models.DateTimeField()
    fecha_vencimiento = models.DateField()
    cantidad = models.PositiveIntegerField() #tiene que hacer la suma en lo que hay en cantidad y el agg de stock de nuevo pedido producto
    nivel_minimo_stock_inventario = models.DecimalField(max_digits=10, decimal_places=2)
    nivel_maximo_stock_inventario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nombre


    


