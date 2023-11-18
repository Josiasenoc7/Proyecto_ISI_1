"""
URL configuration for ProyectoDistribuidora_J_J_J project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DistribuidoraCarne.views import TipoCargoListView,TipoDocumentoListView, CategoriaListView, ClientesListView, EmpleadosListView, ProveedorListView, ProductoListView,ImpuestoListView, EncabezadoFacturaListView, HistorialCargoListView,PrecioHistoricoListView,ParametrosImpuestosListView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('tipoCargo/', TipoCargoListView.as_view(), name='tipos_cargo-list'),
    path('tipoDocumento/', TipoDocumentoListView.as_view(), name='tipo_documentos-list'),
    path('categoria/', CategoriaListView.as_view(), name='categoria-list'),
    path('cliente/', ClientesListView.as_view(), name='cliente-list'),
    path('empleado/', EmpleadosListView.as_view(), name='empleado-list'),
    path('proveedor/', ProveedorListView.as_view(), name='proveedor-list'),
    path('producto/', ProductoListView.as_view(), name='producto-list'),
    path('impuesto/', ImpuestoListView.as_view(), name='impuesto-list'),
    path('encabezado_factura/', EncabezadoFacturaListView.as_view(),name='encabezado_factura-list'),
    path('HistorialCargoListView/', HistorialCargoListView.as_view(), name='historial-cargo-list'),
    path('PrecioHistoricoListView/', PrecioHistoricoListView.as_view(), name='precio-historico-list'),
    path('ParametrosImpuestosListView/', ParametrosImpuestosListView.as_view(), name='parametro-impuesto-list'),

]