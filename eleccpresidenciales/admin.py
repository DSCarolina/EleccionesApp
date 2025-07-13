from django.contrib import admin

# Register your models here.
from .models import Eleccion, Partido, Votante, VotanteEleccion, Candidato

class EleccionAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'descripcion','fecha',)
    ordering = ('fecha',)
    search_fields = ('codigo', 'descripcion',)
admin.site.register(Eleccion, EleccionAdmin)

class PartidoAdmin(admin.ModelAdmin):
    list_display = ('sigla', 'nombre',)
    ordering = ('nombre',)
    search_fields = ('sigla', 'nombre',)
admin.site.register(Partido,PartidoAdmin)

class VotanteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'cedula', 'fecha_nacimiento', 'direccion', 'celular', 'correo', 'fecha_registro')
    ordering = ('nombre','apellido',)
    search_fields = ('nombre','apellido','cedula',)
    
admin.site.register(Votante, VotanteAdmin)

class VotanteEleccionAdmin(admin.ModelAdmin):
    list_display = ('votante', 'eleccion', 'habilitado',)
    ordering = ('votante',)
    list_filter = ('habilitado',)
admin.site.register(VotanteEleccion, VotanteEleccionAdmin)

class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'partido', 'tipo',)
    ordering = ('nombre',)
    search_fields = ('nombre',)
admin.site.register(Candidato,CandidatoAdmin)