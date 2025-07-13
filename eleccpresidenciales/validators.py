from datetime import date
from django.core.exceptions import ValidationError
import re

def valida_numeros(value):
    #Valida que el campo tenga solo números y sea de 8 dígitos
    if not re.search(r'^\d{8}$', value):
        raise ValidationError(
            'El campo solo debe contener 8 números.',)

def valida_sigla(value):
    #Valida que la sigla solo tenga letras mayúsculas y números
    if not re.search(r'^[A-Z0-9]+$', value):
        raise ValidationError("La sigla debe registrarse con texto en mayúsculas.")

def valida_texto_sin_numero(value):
    #Valida que el campo solo tenga texto
    if re.search(r'\d', value):
        raise ValidationError("El nombre no debe contener números.")
    

