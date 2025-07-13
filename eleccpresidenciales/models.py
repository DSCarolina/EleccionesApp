from django.db import models
from uuid import uuid4
from .validators import valida_texto_sin_numero, valida_numeros,valida_sigla

class Eleccion(models.Model):
    codigo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=False, null=False)
    fecha = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.descripcion

class Votante(models.Model):
    nombre = models.CharField(max_length=100,validators=[valida_texto_sin_numero,] )
    apellido = models.CharField(max_length=100,validators=[valida_texto_sin_numero,])
    cedula = models.CharField(max_length=20, unique=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=200)
    celular = models.CharField(max_length=8, blank=True, null=True, validators=[valida_numeros])
    correo = models.EmailField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.cedula}"

class VotanteEleccion(models.Model):
    votante = models.ForeignKey(Votante, on_delete=models.CASCADE)
    eleccion = models.ForeignKey(Eleccion, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.votante} - {self.eleccion}"
    
class Partido(models.Model):
    sigla = models.CharField(max_length=20, validators=[valida_sigla,])
    nombre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre

class TipoCandidato(models.TextChoices):
    PRESIDENTE = 'PRESIDENTE', 'Presidente'
    VICEPRESIDENTE = 'VICEPRESIDENTE', 'Vicepresidente'
    #SE PUEDE AÑADIR OTROS TIPOS DE CANDIDATOS

class Candidato(models.Model):
    nombre = models.ForeignKey(Votante, on_delete=models.CASCADE)
    partido = models.ForeignKey(Partido, on_delete=models.CASCADE)
    tipo = models.CharField(
        max_length=150,
        choices=TipoCandidato.choices
    )
    eleccion = models.ForeignKey(Eleccion, on_delete=models.CASCADE)
    habilitado = models.BooleanField(default=True)
    observaciones = models.TextField(blank=True, null=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre} - {self.partido} ({self.eleccion})"

class Voto(models.Model): 
    eleccion = models.ForeignKey(Eleccion, on_delete=models.CASCADE)
    votante = models.ForeignKey(Votante, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE, blank=True, null=True)
    fecha_voto = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Voto de {self.votante} en {self.eleccion} por {self.candidato}"