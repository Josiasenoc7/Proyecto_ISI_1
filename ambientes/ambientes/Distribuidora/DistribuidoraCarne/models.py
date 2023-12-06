from django.db import models
from django.db.models.signals import m2m_changed
from decimal import Decimal, ROUND_HALF_UP
from DistribuidoraCarne.validaciones import *
from simple_history.models import HistoricalRecords
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save, post_delete
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.utils.timezone  import now
from django.utils import timezone

#UltimoCambio
class MetodosPago(models.Model):
    nombre = models.CharField(max_length=50, validators=[validar_nombre])

    def __str__(self):
        return self.nombre

class TipoDocumento(models.Model):
    nombre = models.CharField(max_length=50, default='Identidad', validators=[validar_nombre])
    def __str__(self):
        return self.nombre
    
class TipoCargo(models.Model):
    nombre = models.CharField(max_length=50, validators=[validar_nombre])

    def __str__(self):
        return self.nombre

   
class Clientes(models.Model):
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.CASCADE, default=1)
    documento = models.CharField(max_length=15, validators=[validar_id])
    nombre_cliente = models.CharField(max_length=65,validators=[validar_nombre])
    apellido_cliente = models.CharField(max_length=65,validators=[validar_nombre])
    telefono = models.CharField(max_length=10, validators=[validar_telefono])
    correo = models.CharField(max_length=50, validators=[validar_correo])
    rtn = models.CharField(max_length=14, validators=[validar_rtn])
    direccion = models.CharField(max_length=150, validators=[validar_direccion])
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        
    def __str__(self):
        return f"{self.nombre_cliente} {self.apellido_cliente}"

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length=65, validators=[validar_nombre])
    estado = models.BooleanField(null=True, validators=[validar_estado])
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre_categoria

class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=65, validators=[validar_nombre])
    telefono = models.CharField(max_length=10, validators=[validar_telefono])
    correo = models.CharField(max_length=50, validators=[validar_correo])
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
    nombre_descuento = models.CharField(max_length=20, unique=True, validators=[validar_nombre])
    descripción = models.CharField(max_length=50,validators=[validar_descripcion])
    valor_descuento = models.DecimalField(max_digits=5, decimal_places=2)
    fecha_creación = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name_plural = "Descuentos"
        verbose_name = "Descuentos" 
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)   
    
    def __str__(self):
        return self.nombre_descuento     
        
class Impuesto(models.Model):
    nombre_impuesto = models.CharField(max_length=20, validators=[validar_nombre])
    descripción = models.CharField(max_length=50,validators=[validar_descripcion])
    valor_impuesto = models.DecimalField(max_digits=5, decimal_places=2,default=00.00, validators=[validar_valor_impuesto])
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
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE,default=1)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE,default=1)
    impuesto = models.ForeignKey(Impuesto, on_delete=models.CASCADE,default=1)    
    descuento = models.ForeignKey(Descuento, on_delete=models.CASCADE,default=1)    
    estado = models.BooleanField(validators=[validar_estado])
    fecha_creacion = models.DateTimeField(auto_now=True)
    history = HistoricalRecords()

    def __str__(self):
        return f"{self.nombre_producto} - {self.categoria}- {self.descuento}- {self.impuesto}"
      
class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField(validators=[validar_fecha_vencimiento])
    cantidad = models.DecimalField(max_digits=10, decimal_places=0,validators=[validar_Cantidad]) 
    Stock_minimo = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_nivel_minimo_stock])
    Stock_maximo = models.DecimalField(max_digits=10, decimal_places=2, validators=[validar_nivel_maximo_stock])
    
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
    telefono = models.CharField(max_length=10, validators=[validar_telefono])
    correo = models.CharField(max_length=50, validators=[validar_correo])
    tipo_cargo = models.ForeignKey(TipoCargo, on_delete=models.CASCADE, default=1)
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE, default=1)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'

    def __str__(self):
        return self.nombre_empleado  

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
    cantidad = models.DecimalField(max_digits=10,default=0, decimal_places=2, validators=[validar_Cantidad])
    precio_compra = models.DecimalField(max_digits=10,default=0, decimal_places=2, validators=[validar_precio])
    sub_total = models.DecimalField(max_digits=10,default=0, decimal_places=2)
    descuento = models.DecimalField(max_digits=10,default=0, decimal_places=2)
    total = models.DecimalField(max_digits=10,default=0, decimal_places=2, validators=[validar_Total_Cotizacion])

    def __str__(self):
        return '{}'.format(self.producto)

    def save(self, *args, **kwargs):
        if self.cantidad is not None and self.precio_compra is not None:
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


class FacturaParametro(models.Model):
    empresa = models.ForeignKey(Sucursal,on_delete=models.CASCADE)
    parametros = models.ForeignKey(ParametroSar,on_delete=models.CASCADE)
    fecha_emision = models.DateTimeField()
    rango_inicial_factura = models.IntegerField()
    rango_final_factura = models.IntegerField()
    cai = models.CharField(max_length=32,unique=True, validators=[validar_cai])
    fecha_creacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.fecha_emision)

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
    
    def cais(self):
        return f"{self.cai[:6]}-{self.cai[6:12]}-{self.cai[12:18]}-{self.cai[18:24]}-{self.cai[24:30]}-{self.cai[30:]}"

    class Meta:
        verbose_name_plural = "Encabezado Facturas"
        verbose_name = "Encabezado Factura"
    
    def relleno_rango_total(self, es_inicial=True):
        rango = self.rango_inicial_factura if es_inicial else self.rango_final_factura
        return str(rango).zfill(8)        
        
  
class FacturaDet(models.Model):
    producto = models.ManyToManyField(Inventario,through='DetalleVenta')
    sub_total = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    descuento = models.DecimalField(max_digits=10,decimal_places=2,default=0)
    impuesto = models.DecimalField(max_digits=10,decimal_places=2,default=0, validators=[validar_valor_impuesto])
    total = models.DecimalField(max_digits=10,default=0, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)


    def __Str__(self):
        return '{}'.format(self.producto)
    
    class Meta:
        verbose_name_plural = "Detalles Facturas"
        verbose_name = "Detalle Factura"
        get_latest_by = 'created_at'   
        

        
class DetalleVenta(models.Model):
    detalle = models.ForeignKey(FacturaDet, on_delete=models.CASCADE)
    producto = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=10,decimal_places=2,default=0, validators=[validar_Cantidad])  
        
    def clean(self):
        super().clean()
        if self.cantidad > self.producto.cantidad:
            raise ValidationError("No se puede vender más de lo que tienes en stock.")
        if self.cantidad < 0:
            raise ValidationError("La cantidad debe ser mayor que 1")
    
    
    @staticmethod
    def get_decimal_value(value):
        try:
            return Decimal(str(value))
        except Exception as e:
            print(f"Error al convertir a decimal: {e}")
            return Decimal('0')
    
    def __Str__(self):
        return '{}'.format(self.producto)
    
    class Meta:
        verbose_name_plural = "Detalles ventas"
        verbose_name = "Detalle Venta"
        
        
@receiver(post_save, sender = DetalleVenta)
def campos_calculados(sender, instance, **kwargs):
    detalleVenta = instance.detalle
    items = DetalleVenta.objects.filter(detalle = detalleVenta)
    sub_total = 0
    impuesto = 0
    descuento = 0
    
    for i in items:
        sub_total += abs(i.cantidad * i.producto.producto.precio_venta)

    for i in items:
        impuesto += abs((i.cantidad * i.producto.producto.precio_venta) * (i.producto.producto.impuesto.valor_impuesto))

    for i in items:
        descuento += abs((i.cantidad * i.producto.producto.precio_venta) * (i.producto.producto.descuento.valor_descuento))
    
    instance.detalle.sub_total = sub_total
    instance.detalle.impuesto = impuesto
    instance.detalle.descuento = descuento
    instance.detalle.total = abs(((instance.detalle.sub_total) - (instance.detalle.descuento)) + (instance.detalle.impuesto))
    instance.detalle.save()

@receiver(post_save, sender=DetalleVenta)
def actualizar_inventario_al_guardar(sender, instance, created, **kwargs):
    if created:
        instance.producto.cantidad = instance.producto.cantidad - instance.cantidad
        instance.producto.save()

@receiver(post_delete, sender=DetalleVenta)
def actualizar_inventario_al_borrar(sender, instance, **kwargs):
    instance.producto.cantidad = instance.producto.cantidad + instance.cantidad
    instance.producto.save()




class Factura(models.Model):
    parametros = models.ForeignKey(FacturaParametro,on_delete=models.CASCADE)
    consecutivo = models.CharField(max_length=40)
    empleado = models.ForeignKey(Empleados,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    tipo_pago = models.ForeignKey(MetodosPago,on_delete=models.CASCADE)
    tarjeta= models.CharField(max_length=16,null=True,blank=True, validators=[validar_numero_tarjeta])
    efectivo= models.CharField(max_length=20,null=True, blank=True)
    hora = models.DateTimeField(default=timezone.now, editable=False)
    fecha_creacion = models.DateTimeField(auto_now=True)
    detalle = models.ForeignKey(FacturaDet,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return str(self.parametros) + ' - ' + str(self.consecutivo) + ' - ' + str(self.cliente)
    
    def incrementar_numero_factura(self):
        ultimaFactura = Factura.objects.filter(parametros=self.parametros).order_by('id').last()
        if self.parametros:
            if not ultimaFactura:
                return self.parametros.rango_inicial_factura

            numeroFactura = int(ultimaFactura.consecutivo)
            rangoFinal = int(self.parametros.rango_final_factura)

            if numeroFactura >= rangoFinal:
                return None
            else:
                NuevaFactura = numeroFactura + 1
                return str(NuevaFactura).zfill(8)
    
    def clean(self):
        super().clean()
        consecutivo = self.incrementar_numero_factura()
        if consecutivo is None:
            raise ValidationError(("Se ha alcanzado el rango final de facturación. No se generará una nueva factura."), code='rango_final_factura')



     
class Rutas(models.Model):
    ruta = models.CharField(max_length=50, validators=[validar_descripcion])

    def __str__(self):
        return str(self.ruta)




    class Meta:
        verbose_name = 'Ruta'
        verbose_name_plural = 'Rutas'
    
class Transporte(models.Model):
    ruta = models.ForeignKey(Rutas, on_delete=models.CASCADE,default=1)
    nombre_carro = models.CharField(max_length=50, validators=[validar_nombre])
    codigo = models.CharField(max_length=50, validators=[validar_placa_honduras])
    chofer = models.ForeignKey(Empleados, on_delete=models.CASCADE,default=1)

    def __str__(self):
        try:
            return str(self.ruta)
        except Exception as e:
            return f"Error al representar la ruta: {e}"

    
class Entrega(models.Model):
    carro = models.ForeignKey(Transporte, on_delete=models.CASCADE, default=1)
    fecha_entrega = models.DateField(null=True, blank=True, validators=[validar_fecha_no_pasado])
    hora_entrega = models.TimeField(null=True, blank=True)
    direccion_entrega = models.CharField(max_length=255, null=True, blank=True, validators=[validar_direccion])
    def __str__(self):
        return str(self.direccion_entrega)

class Devoluciones(models.Model):
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE,default=1)
    cantidad = models.IntegerField(validators=[validar_Cantidad])
    descripcion = models.CharField(max_length=255,validators=[validar_descripcion])
    fecha_devolucion = models.DateField(validators=[validar_date_time])

@receiver(post_save, sender=Devoluciones)
def aumentar_stock(sender, instance, created, **kwargs):
    if created:  # Asegurarse de que sea una nueva devolución
        producto_devuelto = instance.id_producto
        cantidad_devuelta = instance.cantidad

        inventario_producto = Inventario.objects.get(producto=producto_devuelto)
        inventario_producto.cantidad += cantidad_devuelta
        inventario_producto.save()

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
        return str(self.id_cliente)  # Devuelve una representación de cadena del objeto Clientes

    

class Pedido(models.Model):
    id_clientes = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    fecha_pedido = models.DateTimeField()
    total_pedido = models.FloatField(validators=[validar_total_pedido])
 

    def __str__(self):
        return str(self.fecha_pedido)
