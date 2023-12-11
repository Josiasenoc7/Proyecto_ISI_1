from django.shortcuts import render
from django.views.generic import DetailView
from .models import *

# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.views import generic
from django.views.generic import ListView
from .models import *
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.http import HttpResponse

class FacturaListView(ListView):
    model = Factura
    template_name = "factura.html"
    context_object_name = 'facturas'


def descargar_pdf_factura(request, id):
    try:
        factura_obj = Factura.objects.get(id=id)
        detalles_factura = FacturaDet.objects.filter(id=factura_obj.detalle.id)
        detalles_venta = DetalleVenta.objects.filter(detalle=factura_obj.detalle)

        sucursal_code = str(factura_obj.empleado.sucursal.id).zfill(3)

        context = {
            'encabezado': {
                'consecutivo': factura_obj.consecutivo,
                'rtn': factura_obj.empleado.sucursal.rtn,
                'fechaPago': factura_obj.hora,
                'horafactura': factura_obj.hora,
                'cliente': factura_obj.cliente,
                'cai': factura_obj.parametros.cai,
                'numero_inicio': factura_obj.parametros.ParametroSar.numero_inicio,
                'numero_final': factura_obj.parametros.ParametroSar.numero_fin,
                'sucursal': sucursal_code,
                'sucursal_name': factura_obj.empleado.sucursal.names,
                'direccion_sucursal': factura_obj.empleado.sucursal.direccionSu,
                'empleado': factura_obj.empleado,
                'parametros': factura_obj.parametros,
            },
            'detalles_factura': detalles_factura,
            'detalles_venta': detalles_venta,
        }

        template = get_template('factura.html')
        html_content = template.render(context)

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="factura_{id}.pdf"'
        pdf_status = pisa.CreatePDF(html_content, dest=response)

        if pdf_status.err:
            return HttpResponse('Error al generar el PDF')

        return response

    except Factura.DoesNotExist:
        return HttpResponse('Factura no encontrada.', status=404)

def lockout(request, credentials, *args, **kwargs):
    return JsonResponse({"status": "Cuenta bloqueada por intentos fallidos de acceso"}, status=403)

class FacturaDetailView(DetailView):
    model = Factura
    template_name = 'factura_detail.html'
    context_object_name = 'factura'
