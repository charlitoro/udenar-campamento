from django.contrib import admin
from register.models import Estudiante, Registro

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('num_manilla', 'codigo', 'cedula', 'nombre', 'programa', 'telefono', 'familiar', 'tel_familiar', 'photo')
    list_display_links = ('num_manilla',)
    list_editable = ('nombre', 'programa', 'telefono', 'familiar', 'tel_familiar', 'photo')
    search_fields = ('num_manilla', 'cedula', 'codigo', 'nombre')
# Register your models here.

@admin.register(Registro)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('pk', 'estudiante', 'ingreso', 'salida')
    list_display_links = ('pk', 'estudiante')
    list_editable = ('ingreso', 'salida')
    search_fields = ('estudiante__nombre',  'estudiante__codigo', 'estudiante__cedula')