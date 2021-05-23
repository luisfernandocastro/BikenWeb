from django.contrib import admin
from .models import *

@admin.register (Persona)
class PersonaAdmin(admin.ModelAdmin):
    list_display =  ('nombres','apellidos','correoelectronico')
    search_fields = ['nombres']
    list_editable = ['apellidos']
    list_filter = ['nombres','correoelectronico']
    list_per_page = 10

    pass

@admin.register (Bicicletas)
class BicletasAdmin(admin.ModelAdmin):
    # list_display =  ('precioalquiler','categoria','material')
    # search_fields = ['nombres']
    # list_editable = ['apellidos']
    # list_filter = ['nombres','correoelectronico']
    # list_per_page = 10
    pass

@admin.register (Pagos)
class PagosAdmin(admin.ModelAdmin):
    # list_display =  ('nombres','apellidos','correoelectronico')
    # search_fields = ['nombres']
    # list_editable = ['apellidos']
    # list_filter = ['nombres','correoelectronico']
    # list_per_page = 10
    pass

@admin.register (Tipopersona)
class PersonaAdmin(admin.ModelAdmin):
    # list_display =  ('nombres','apellidos','correoelectronico')
    # search_fields = ['nombres']
    # list_editable = ['apellidos']
    # list_filter = ['nombres','correoelectronico']
    # list_per_page = 10
    pass

@admin.register (Catalogo)
class CatalogoAdmin(admin.ModelAdmin):
    # list_display =  ('nombres','apellidos','correoelectronico')
    # search_fields = ['nombres']
    # list_editable = ['apellidos']
    # list_filter = ['nombres','correoelectronico']
    # list_per_page = 10
    pass

@admin.register (Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # list_display =  ('nombres','apellidos','correoelectronico')
    # search_fields = ['nombres']
    # list_editable = ['apellidos']
    # list_filter = ['nombres','correoelectronico']
    # list_per_page = 10
    pass


@admin.register (Contrato)
class ContratoAdmin(admin.ModelAdmin):
    # list_display =  ('nombres','apellidos','correoelectronico')
    # search_fields = ['nombres']
    # list_editable = ['apellidos']
    # list_filter = ['nombres','correoelectronico']
    # list_per_page = 10
    pass

@admin.register (Modulo)
class ModuloAdmin(admin.ModelAdmin):
    # list_display =  ('nombres','apellidos','correoelectronico')
    # search_fields = ['nombres']
    # list_editable = ['apellidos']
    # list_filter = ['nombres','correoelectronico']
    # list_per_page = 10
    pass

@admin.register (Perfilusuario)
class PerfilusuarioAdmin(admin.ModelAdmin):
    # list_display =  ('nombres','apellidos','correoelectronico')
    # search_fields = ['nombres']
    # list_editable = ['apellidos']
    # list_filter = ['nombres','correoelectronico']
    # list_per_page = 10
    pass

@admin.register (Privilegios)
class PrivilegiosAdmin(admin.ModelAdmin):
    # list_display =  ('nombres','apellidos','correoelectronico')
    # search_fields = ['nombres']
    # list_editable = ['apellidos']
    # list_filter = ['nombres','correoelectronico']
    # list_per_page = 10

    pass

@admin.register (Reserva)
class ReservaAdmin(admin.ModelAdmin):
    # list_display =  ('nombres','apellidos','correoelectronico')
    # search_fields = ['nombres']
    # list_editable = ['apellidos']
    # list_filter = ['nombres','correoelectronico']
    # list_per_page = 10
    pass

@admin.register (Tipocontrato)
class TipocontratoAdmin(admin.ModelAdmin):
    # list_display =  ('nombres','apellidos','correoelectronico')
    # search_fields = ['nombres']
    # list_editable = ['apellidos']
    # list_filter = ['nombres','correoelectronico']
    # list_per_page = 10
    pass






