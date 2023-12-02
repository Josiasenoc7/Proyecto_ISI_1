from django.db import models
from django.db.models.signals import m2m_changed
from decimal import Decimal, ROUND_HALF_UP
from DistribuidoraCarne.validaciones import *
from simple_history.models import HistoricalRecords
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from django import forms
from django.core.exceptions import ObjectDoesNotExist



class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50, default='Identidad')
    def __str__(self):
        return self.nombre
    
class TipoCargo(models.Model):
    nombre = models.CharField(max_length=50, validators=[validar_nombre])

    def __str__(self):
        return self.nombre

class Correo(models.Model):
    correo = models.CharField(max_length=50, validators=[validar_correo])

    def __str__(self):
        return self.correo

class Telefono(models.Model):
    telefono = models.CharField(max_length=10, validators=[validar_telefono])

    def __str__(self):
        return self.telefono
   
class Clientes(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, default=1)
    documento = models.CharField(max_length=15, validators=[validar_id])
    nombre_cliente = models.CharField(max_length=65,validators=[validar_nombre])
    apellido_cliente = models.CharField(max_length=65,validators=[validar_nombre])
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE, default=1)
    correo = models.ForeignKey(Correo, on_delete=models.CASCADE, default=1)
    rtn = models.CharField(max_length=14, validators=[validar_rtn])
    direccion = models.CharField(max_length=150, validators=[validar_direccion])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
        def __str__(self):
            return self.nombre_cliente

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=65, validators=[validar_nombre])
    estado = models.BooleanField(null=True, validators=[validar_estado])
    fecha_creacion = models.DateTimeField(auto_now_add=True)

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
    fecha_creacion = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'

    def __str__(self):
        return self.nombre_proveedor
    
class Descuento(models.Model):
    nombre_descuento = models.CharField(max_length=50, unique=True)
    descripción = models.CharField(max_length=50,validators=[validar_descripcion])
    valor_descuento = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creación = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Descuentos"
        verbose_name = "Descuentos" 
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)   
    
    def _str_(self):
        return self.nombre_descuento     
        
class Impuesto(models.Model):
    nombre_impuesto = models.CharField(max_length=20)
    descripción = models.CharField(max_length=50,validators=[validar_descripcion])
    valor_impuesto = models.DecimalField(max_digits=5, decimal_places=2,default=00.00)
    fecha_creación = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.nombre_impuesto} - {self.descripción}"

    class Meta:
        db_table = 'impuesto'
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        
@receiver(pre_save, sender=Impuesto)
def impuesto_previo(sender, instance, **kwargs):
    if instance._state.adding:
        instance.fecha_creación = timezone.now()
    
class Producto(models.Model):
    nombre_producto = models.CharField(max_length=50, validators=[validar_nombre])
    descripcion = models.CharField(max_length=255,validators=[validar_descripcion])
    precio_venta = models.DecimalField(max_digits=10, decimal_places=2,default=200, validators=[validar_precio])
    stock = models.PositiveIntegerField(validators=[validar_stock_actual])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,default=1)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE,default=1)
    impuesto = models.ForeignKey(Impuesto, on_delete=models.CASCADE,default=1)    
    #agg models descuento con FK
    descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE,default=1)    
    estado = models.BooleanField(validators=[validar_estado])
    fecha_creacion = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.nombre_producto
      
class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField(validators=[validar_fecha_vencimiento])
    cantidad = models.PositiveIntegerField(validators=[validar_Cantidad]) 
    Stock_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    Stock_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"{self.producto}"
    
class Sucursal(models.Model):
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    nombre_sucursal = models.CharField(max_length=65, validators=[validar_nombre])
    ciudad = models.CharField(max_length=65, validators=[validar_nombre])
    direccion = models.CharField(max_length=255, validators=[validar_direccion])
    telefono = models.CharField(max_length=8, validators=[validar_telefono])
    rtn= models.CharField(max_length=14, validators=[validar_rtn])
    fecha_creacion = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.nombre_sucursal

    class Meta:
        verbose_name = 'Surcusal'
        verbose_name_plural = 'Surcusales'  
    
 
class Empleados(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, default=1)
    documento = models.CharField(max_length=15)
    nombre_empleado = models.CharField(max_length=65, validators=[validar_nombre])
    apellido_empleado = models.CharField(max_length=65, validators=[validar_nombre])
    fecha_nacimiento = models.DateField(validators=[validar_fecha_nacimiento])
    telefono = models.ForeignKey(Telefono, on_delete=models.CASCADE, default=1)
    correo = models.ForeignKey(Correo, on_delete=models.CASCADE, default=1)
    tipo_cargo = models.ForeignKey(TipoCargo, on_delete=models.CASCADE, default=1)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre_empleado  

class EmpleadosForm(forms.ModelForm):
    class Meta:
        model = Empleados
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        tipos_cargo_exist = TipoCargo.objects.all()
        self.fields['tipo_cargo'].queryset = tipos_cargo_exist  


class ComprasEncabezado(models.Model):
    proveedor=models.ForeignKey(Proveedor,on_delete=models.CASCADE)
    no_factura=models.CharField(max_length=100)
    fecha_compra=models.DateField(null=True,blank=True, validators=[validar_date_time])
    observacion=models.TextField(blank=True,null=True, validators=[validar_descripcion])

    def __str__(self):
        return '{}'.format(self.observacion)

    def save(self):
        self.observacion = self.observacion.upper()
        super(ComprasEncabezado,self).save()

class ComprasDetalle(models.Model):
    compra = models.ForeignKey(ComprasEncabezado, on_delete=models.CASCADE)
    producto = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    precio_compra = models.FloatField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    total = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self, *args, **kwargs):
        self.sub_total = float(self.cantidad) * float(self.precio_compra)
        self.total = self.sub_total - float(self.descuento)
        super(ComprasDetalle, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Detalles Compras"
        verbose_name = "Detalle Compra"


@receiver(post_save, sender=ComprasDetalle)
def aumentar_inventario_postSave(sender, instance, created, **kwargs):
    if created:
        instance.producto.cantidad += instance.cantidad
        instance.producto.save()

class ParametroSar(models.Model):
    numero_inicio= models.CharField(max_length=5,default='0001')
    numero_fin= models.CharField(max_length=5,default='0005')

    class Meta:
        verbose_name = "Parámetros de Sar"
        verbose_name_plural = "Parámetros de Sar"

    def __str__(self):
        return f"{self.numero_inicio} - {self.numero_fin}"     


class FacturaEncabezado(models.Model):
    Empresa = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField()
    rango_inicial_factura = models.IntegerField()
    rango_final_factura = models.IntegerField()
    cai = models.CharField(max_length=32,validators=[validar_cai],unique=True)
    parametros = models.ForeignKey(ParametroSar,on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.fecha_emision)

    class Meta:
        verbose_name_plural = "Encabezado Facturas"
        verbose_name = "Encabezado Factura"

        
        
        
  
class FacturaDet(models.Model):
    factura = models.ForeignKey(FacturaEncabezado, on_delete=models.CASCADE)
    producto = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.BigIntegerField(default=0)
    sub_total = models.FloatField(default=0)
    descuento = models.FloatField(default=0)
    impuesto = models.ForeignKey(Impuesto, on_delete=models.CASCADE,default=1) 
    total = models.FloatField(default=0)

    def __str__(self):
        return '{}'.format(self.producto)

    
    class Meta:
        verbose_name_plural = "Detalles Facturas"
        verbose_name="Detalle Factura"
        

    def precio(self):
        return self.cantidad * self.producto.producto.precio_venta
    
    def impuestos(self):
        impuesto = self.producto.producto.impuesto.valor_impuesto if self.producto.producto.impuesto else 0
        result = (self.cantidad * self.producto.producto.precio_venta) * impuesto
        result = result.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        self.impuesto = result  # Guardar el valor del impuesto en el campo del modelo
        return result
    
    def descuentos(self):
        result = (self.cantidad * self.producto.producto.precio_venta) * self.producto.producto.descuento.valor_descuento
        result = result.quantize(Decimal('0.00'), rounding=ROUND_HALF_UP)
        return result
    

def get_decimal_value(value):
    try:
        return Decimal(str(value))
    except Exception as e:
        print(f"Error al convertir a decimal: {e}")
        return Decimal('0')

@receiver(post_save, sender=FacturaDet)
def calcular_Campos(sender, instance, **kwargs):
    factura = instance.factura
    detalles_factura = FacturaDet.objects.filter(factura=factura)
    
    impuesto_total = Decimal('0')
    descuento_total = Decimal('0')
    subtotal_total = Decimal('0')
    
    for detalle in detalles_factura:
        subtotal_total += abs(detalle.cantidad * Decimal(str(detalle.producto.producto.precio_venta)))
        descuento_total += abs(get_decimal_value(detalle.descuento))
        impuesto_total += abs(get_decimal_value(detalle.impuesto))
    
    factura.sub_total = subtotal_total
    factura.impuesto = impuesto_total
    factura.descuento = descuento_total
    factura.total = abs(subtotal_total + impuesto_total - descuento_total)
    factura.save()

@receiver(post_save, sender=FacturaDet)
def aumentar_inventario_postSave(sender, instance, created, **kwargs):
    if created:
        inventario = instance.producto  
        producto = inventario.producto  
        producto.stock += instance.cantidad
        producto.save()

@receiver(post_delete, sender=FacturaDet)
def aumentar_inventario_postDelete(sender, instance, **kwargs):
    producto = instance.producto  # Acceder al producto desde FacturaDet
    if hasattr(producto, 'inventario'):  # Verificar si el producto tiene relación con Inventario
        inventario = producto.inventario  # Obtener el Inventario relacionado con el Producto
        inventario.cantidad += instance.cantidad
        inventario.save()

     

















class Rutas(models.Model):
    ruta = models.CharField(max_length=50)
    def _str_(self):
        return self.ruta
    
class Transporte(models.Model):
    ruta = models.ForeignKey(Rutas, on_delete=models.CASCADE,default=1)
    nombre_carro = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    chofer = models.ForeignKey(Empleados, on_delete=models.CASCADE,default=1)

    def _str_(self):
        return self.ruta
    
class Entrega(models.Model):
    carro = models.ForeignKey(Transporte, on_delete=models.CASCADE, default=1)
    fecha_entrega = models.DateField(null=True, blank=True)
    hora_entrega = models.TimeField(null=True, blank=True)
    direccion_entrega = models.CharField(max_length=255, null=True, blank=True, validators=[validar_direccion])
    def _str_(self):
        return str(self.direccion_entrega)

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
    fecha_cotizacion = models.DateField(validators=[validar_fecha_actualizacion])
   
    class Meta:
        verbose_name = 'Cotizacion'
        verbose_name_plural = 'Cotizaciones'  
    

    def str(self):
        return self.id_cliente
    
class MetodoPago(models.Model):   
    tipo_metodo_pago = models.CharField(max_length=20, validators=[validar_nombre])    
    def _str_(self):
        return str(self.tipo_metodo_pago)
    
class Pedido(models.Model):
    id_clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField()
    total_pedido = models.FloatField(validators=[validar_total_pedido])
 

    def _str_(self):
        return str(self.fecha_pedido)