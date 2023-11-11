import re
from datetime import date
from django.core.exceptions import ValidationError
from django.utils import timezone


def validar_nombre(nombre):
    letras = sum(c.isalpha() for c in nombre)
    if letras < 3:
        raise ValidationError('El nombre debe contener al menos 3 letras.')
    if re.search(r'\d', nombre):
        raise ValidationError('El nombre no puede contener números.')

    if re.search(r'(\w)\1\1', nombre):
        raise ValidationError('El nombre no puede contener tres letras repetidas.')

    if re.search(r'\s{3,}', nombre):
        raise ValidationError('El nombre no puede contener más de dos espacios de separación.')
    
    if re.search('[^a-zA-Z0-9 ]', nombre):
        raise ValidationError('El nombre no puede contener caracteres especiales ni signos de puntuación.')

def validar_correo(correo):
    # Comprueba el formato del correo electrónico
    if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', correo):
        raise ValidationError('El correo electrónico no tiene un formato válido.')

    # Comprueba el número de dominios
    domains = correo.split('@')[1].split('.')
    domain_count = len(domains)
    if domain_count < 1 or domain_count > 3:
        raise ValidationError('El correo electrónico debe contener entre 1 y 3 dominios.')

def validar_telefono(telefono):
    if not telefono.isdigit():
        raise ValidationError('El número de teléfono solo debe contener números.')

    if len(telefono) != 8:
        raise ValidationError('El número de teléfono debe tener exactamente 8 dígitos.')

    if not re.match(r'^[23789]', telefono):
        raise ValidationError('El número de teléfono debe comenzar con 2, 3,7, 8 o 9.')

def validar_direccion(direccion):
    letras = sum(c.isalpha() for c in direccion)
    if letras < 3:
        raise ValidationError('La dirección debe contener al menos 3 letras.')

def validar_fecha_nacimiento(fecha_nacimiento):
    # Validación de fecha futura
    if fecha_nacimiento > timezone.now().date():
        raise ValidationError('La fecha de nacimiento no puede ser en el futuro.')

    # Validación de edad mínima
    edad_minima = date.today() - date(fecha_nacimiento.year, fecha_nacimiento.month, fecha_nacimiento.day)
    if edad_minima.days < 18 * 365:  # Por ejemplo, requiere ser mayor de 18 años
        raise ValidationError('Debes ser mayor de 18 años.')

    # Validación de rango de fechas
    fecha_minima = date(1900, 1, 1)
    fecha_maxima = date.today()
    if not (fecha_minima <= fecha_nacimiento <= fecha_maxima):
        raise ValidationError('La fecha de nacimiento debe estar entre 01/01/1900 y la fecha actual.')

    # Validación de formato personalizado
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', fecha_nacimiento.strftime('%d/%m/%Y')):
        raise ValidationError('El formato de la fecha de nacimiento debe ser dd/mm/aaaa.')

def validar_salario(salario):
    # Validación de salario negativo
    if salario < 0:
        raise ValidationError('El salario no puede ser negativo.')

    # Validación de salario mínimo
    salario_minimo = 1000  # Ajusta esto al salario mínimo requerido
    if salario < salario_minimo:
        raise ValidationError('El salario no puede ser menor que el salario mínimo.')

    # Validación de salario máximo
    salario_maximo = 150000  # Ajusta esto al salario máximo permitido
    if salario > salario_maximo:
        raise ValidationError('El salario no puede ser mayor que el salario máximo.')

def validar_cargo(cargo):
    errores = []

    # Validación de longitud del cargo
    if len(cargo) < 2:
        errores.append("El cargo debe tener al menos 2 caracteres.")

    # Validación de longitud máxima del cargo
    if len(cargo) > 50:
        errores.append("El cargo no puede tener más de 50 caracteres.")

def validar_descripcion(descripcion):
    # Verificar que la descripción contenga al menos 3 letras.
    letras = sum(c.isalpha() for c in descripcion)
    if letras < 3:
        raise ValidationError('La descripción debe contener al menos 3 letras.')

    # Verificar que no se escriba la misma letra tres veces seguidas.
    prev_letra = None
    repeticiones = 1
    for letra in descripcion:
        if letra == prev_letra:
            repeticiones += 1
            if repeticiones >= 3:
                raise ValidationError('No se permiten tres letras idénticas seguidas.')
        else:
            repeticiones = 1
        prev_letra = letra

def validar_estado(estado):
    errores = []

    # Validar que el estado sea un booleano
    if not isinstance(estado, bool):
        errores.append("El estado debe ser un valor booleano (True o False).")

    # Opcional: Validar que el estado no sea None
    if estado is None:
        errores.append("El estado no puede ser None.")

    # Opcional: Validar que el estado sea True o False
    if estado is not True and estado is not False:
        errores.append("El estado debe ser True o False.")

    # Opcional: Validar que el estado sea True o False usando un enfoque de lista
    if estado not in [True, False]:
        errores.append("El estado debe ser True o False.")

    if errores:
        return errores  # Devolver una lista de errores si hubo problemas
    else:
        return None  # Devolver None si el estado es válido

def validar_nivel_actual_stock(nivel_actual_stock):
        errores = []

        # Validar que el nivel_actual_stock sea un valor positivo o cero.
        if nivel_actual_stock <= 0:
            errores.append("El nivel actual de stock no puede ser negativo.")
        
        # Validar que el nivel_actual_stock no sea mayor que un valor máximo.
        valor_maximo_permitido = 10000 # Reemplaza esto con tu valor máximo permitido.
        if nivel_actual_stock > valor_maximo_permitido:
            errores.append(f"El nivel actual de stock no puede superar {valor_maximo_permitido}.")

        # Validar que el nivel_actual_stock esté en un rango específico.
        rango_minimo = 0
        rango_maximo = 500
        if not rango_minimo <= nivel_actual_stock <= rango_maximo:
            errores.append(f"El nivel actual de stock debe estar entre {rango_minimo} y {rango_maximo}.")

        # Validar que el nivel_actual_stock sea un número entero.
        if not isinstance(nivel_actual_stock, int):
            errores.append("El nivel actual de stock debe ser un número entero.")

        if errores:
            raise ValidationError(errores)  # Lanzar una excepción con la lista de errores si hubo problemas

def validar_nivel_maximo_stock(nivel_maximo_stock):
    errores = []

    # Validar que el nivel_maximo_stock sea un valor positivo o cero.
    if nivel_maximo_stock < 0:
        errores.append("El nivel máximo de stock no puede ser negativo.")

    # Validar que el nivel_maximo_stock no sea mayor que un valor máximo.
    valor_maximo_permitido = 10000 # Reemplaza esto con tu valor máximo permitido.
    if nivel_maximo_stock > valor_maximo_permitido:
        errores.append(f"El nivel máximo de stock no puede superar {valor_maximo_permitido}.")

    # Validar que el nivel_maximo_stock sea un número entero.
    if not isinstance(nivel_maximo_stock, int):
        errores.append("El nivel máximo de stock debe ser un número entero.")

    if errores:
        raise ValidationError(errores)  # Lanzar una excepción con la lista de errores si hubo problemas
    
def validar_nivel_minimo_stock(nivel_minimo_stock):
    errores = []

    # Validar que el nivel_minimo_stock sea un valor no negativo.
    if nivel_minimo_stock < 0:
        errores.append("El nivel mínimo de stock no puede ser negativo.")

    # Validar que el nivel_minimo_stock sea un número entero.
    if not isinstance(nivel_minimo_stock, int):
        errores.append("El nivel mínimo de stock debe ser un número entero.")

    if errores:
        raise ValidationError(errores)  # Lanzar una excepción con la lista de errores si hubo problemas
    
def validar_precioventa(precioventa):
    errores = []

    # Validar que el precio de venta sea un valor no negativo.
    if precioventa < 0:
        errores.append("El precio de venta no puede ser negativo.")

    # Validar que el precio de venta sea un número decimal o entero.

    # Validar que el precio de venta tenga un máximo de 2 decimales.
    if isinstance(precioventa, float) and int(precioventa * 100) != precioventa * 100:
        errores.append("El precio de venta no puede tener más de 2 decimales.")

    # Otras validaciones personalizadas, si es necesario
    # Por ejemplo, verificar si el precio es válido para un rango específico.

    if errores:
        raise ValidationError(errores)  # Lanzar una excepción con la lista de errores si hubo problemas
    
def validar_stock(stock):
    errores = []

    # Validar que el stock sea un valor no negativo.
    if stock < 0:
        errores.append("El stock no puede ser negativo.")
    
    # Validar que el stock no exceda un valor máximo (opcional).
    valor_maximo = 10000  # Puedes ajustar este valor según tus necesidades.
    if stock > valor_maximo:
        errores.append(f"El stock no puede exceder {valor_maximo} unidades.")

    # Otras validaciones personalizadas, si es necesario.
    # Por ejemplo, verificar si el stock es válido para tu negocio.

    if errores:
        raise ValidationError(errores)  # Lanzar una excepción con la lista de errores si hubo problemas

def validar_rtn(rtn):
    errores = []

    # Validar que el RTN tenga exactamente 13 caracteres.
    if len(rtn) != 14:
        errores.append("El RTN debe tener exactamente 14 caracteres.")

    # Validar que el RTN contenga solo dígitos.
    if not rtn.isdigit():
        errores.append("El RTN debe contener solo dígitos (números).")


    # Otras validaciones personalizadas, si es necesario.
    # Por ejemplo, verificar si el RTN es válido según las reglas fiscales de tu país.

    if errores:
        raise ValidationError(errores)  # Lanzar una excepción con la lista de errores si hubo problemas

def validar_total_pedido(pedido):
    # Validación de salario negativo
    if pedido < 0:
        raise ValidationError('El pedido no puede ser negativo.')

def validar_date_time(date_time):
    # Validación de fecha futura
    if date_time > timezone.now().date():
        raise ValidationError('La fecha de creación no puede ser en el futuro.')
    if date_time < timezone.now().date(): 
        raise ValidationError("La fecha de registro no puede ser en el pasado.")
    
def validar_fecha_actualizacion(date_time):
    # Validación de fecha futura
    if date_time > timezone.now().date():
        raise ValidationError('La fecha de creación no puede ser en el futuro.')

def validar_salario_base(salario):
    errores = []

    # Validar que el precio de venta sea un valor no negativo.
    if salario < 0:
        errores.append("El salario base no puede ser negativo.")

def validar_stock_actual(stock_actual):
    errores = []

    # Validar que el precio de venta sea un valor no negativo.
    if stock_actual< 0:
        errores.append("El stock actual no puede ser negativo.")

def validar_id(id):
    errores = []

    # Validar que el RTN tenga exactamente 13 caracteres.
    if len(id) != 14:
        errores.append("El id debe tener exactamente 13 caracteres.")

    # Validar que el RTN contenga solo dígitos.
    if not id.isdigit():
        errores.append("El id debe contener solo dígitos (números).")
 
def validar_Cantidad(Cantidad):
    errores = []

    # Validar que el precio de venta sea un valor no negativo.
    if Cantidad< 0:
        errores.append("La cantidad no puede ser un valor negativo.")

def validar_Total_Cotizacion(Total_Cotizacion):
    errores = []

    # Validar que el precio de venta sea un valor no negativo.
    if Total_Cotizacion< 0:
        errores.append("El total de la cotizacion no puede ser un valor negativo.")

def validar_numero_tarjeta(numero_tarjeta):
    numero_tarjeta_sin_formato = re.sub(r'\s|-', '', numero_tarjeta)

    if not numero_tarjeta_sin_formato.isdigit():
        raise ValidationError('El número de tarjeta debe contener solo dígitos.')

    longitud_esperada = 16
    if len(numero_tarjeta_sin_formato) != longitud_esperada:
        raise ValidationError(f'El número de tarjeta debe tener {longitud_esperada} dígitos.')

    # Aplicar el algoritmo de Luhn
    digitos = list(map(int, numero_tarjeta_sin_formato[::-1]))
    suma = 0

    for i in range(len(digitos)):
        if i % 2 == 1:
            digito_doble = digitos[i] * 2
            suma += digito_doble if digito_doble < 10 else digito_doble - 9
        else:
            suma += digitos[i]

    if suma % 10 != 0:
        raise ValidationError('El número de tarjeta no es válido según el algoritmo de Luhn.')
    
    return numero_tarjeta_sin_formato

def validar_fecha_vencimiento(fecha_vencimiento):
    # Verificar si la fecha de vencimiento es posterior a la fecha actual
    if fecha_vencimiento < date.today():
        raise ValidationError('La fecha de vencimiento no puede ser en el pasado.')

    # Verificar si la fecha de vencimiento no está en el presente
    if fecha_vencimiento == date.today():
        raise ValidationError('La fecha de vencimiento no puede ser la fecha actual.')

    # Verificar si la fecha de vencimiento cumple con el formato MM/YY
    if not re.match(r'^\d{2}/\d{2}$', fecha_vencimiento.strftime('%m/%y')):
        raise ValidationError('La fecha de vencimiento debe tener el formato MM/YY.')

    return fecha_vencimiento

def validar_cvv(cvv):
    # Verificar que el CVV sea numérico y tenga la longitud esperada (puedes ajustar según sea necesario)
    if not cvv.isdigit():
        raise ValidationError('El CVV debe contener solo dígitos.')

    longitud_esperada = 3  # Puedes ajustar esto para CVV de 4 dígitos si es necesario
    if len(cvv) != longitud_esperada:
        raise ValidationError(f'El CVV debe tener {longitud_esperada} dígitos.')

    return cvv

def validar_nombre_titular(nombre):
    letras = sum(c.isalpha() for c in nombre)
    if letras < 1:
        raise ValidationError('El nombre debe contener al menos 1 letras.')
    if re.search(r'\d', nombre):
        raise ValidationError('El nombre no puede contener números.')

    if re.search(r'(\w)\1\1', nombre):
        raise ValidationError('El nombre no puede contener tres letras repetidas.')

    if re.search(r'\s{3,}', nombre):
        raise ValidationError('El nombre no puede contener más de dos espacios de separación.')
    
    if re.search('[^a-zA-Z0-9 ]', nombre):
        raise ValidationError('El nombre no puede contener caracteres especiales ni signos de puntuación.')

def validar_valor_impuesto(valor):
    try:
        # Intentar convertir la entrada a un número decimal
        valor_decimal = float(str(valor).replace(',', '.'))

        # Verificar que el valor del impuesto sea un número decimal positivo
        if not isinstance(valor_decimal, (int, float)) or valor_decimal < 0:
            raise ValidationError('El valor del impuesto debe ser un número decimal positivo.')

        # Verificar que el valor tenga como máximo dos decimales
        cantidad_decimales = len(str(valor_decimal).split('.')[-1])
        if cantidad_decimales > 2:
            raise ValidationError('El valor del impuesto debe tener como máximo dos decimales.')

        # Verificar que el valor tenga como máximo 5 dígitos en total
        if len(str(valor_decimal).replace('.', '')) > 5:
            raise ValidationError('El valor del impuesto no puede tener más de 5 dígitos en total.')

    except ValueError:
        raise ValidationError('El valor del impuesto no es válido.')

    return valor

def validar_nombre_negocio(nombre):
    letras = sum(c.isalpha() for c in nombre)
    if letras < 3:
        raise ValidationError('El nombre debe contener al menos tres letras.')
    if re.search(r'\d', nombre):
        raise ValidationError('El nombre no puede contener números.')

    if re.search(r'(\w)\1\1\1', nombre):
        raise ValidationError('El nombre no puede contener cuatro letras repetidas.')

    if re.search(r'\s{3,}', nombre):
        raise ValidationError('El nombre no puede contener más de dos espacios de separación.')
    
    if re.search('[^a-zA-Z0-9 ]', nombre):
        raise ValidationError('El nombre no puede contener caracteres especiales ni signos de puntuación.')
