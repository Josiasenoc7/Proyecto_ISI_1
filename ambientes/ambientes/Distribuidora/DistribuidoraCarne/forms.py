from django import forms
from .models import *
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Asegúrate de agregar esta línea

class FacturaDetForm(forms.ModelForm):
    class Meta:
        model = FacturaDet
        fields = '__all__'


class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta
        fields = '__all__'
        
        



