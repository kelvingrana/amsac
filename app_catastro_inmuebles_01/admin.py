from django.contrib import admin
from .models import Usuario, Etapa, Tramite

# Registrar el modelo Usuario en el panel de administración
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'rol', 'is_active', 'date_joined')
    search_fields = ('username', 'email', 'rol')
    list_filter = ('rol', 'is_active')

admin.site.register(Usuario, UsuarioAdmin)

# Registrar el modelo Etapa en el panel de administración
class EtapaAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

admin.site.register(Etapa, EtapaAdmin)

# Registrar el modelo Tramite en el panel de administración
class TramiteAdmin(admin.ModelAdmin):
    list_display = ('no_oficio', 'etapa', 'inspector_responsable', 'fecha_recepcion', 'fecha_vencimiento', 'get_estado')
    search_fields = ('no_oficio', 'comentarios')
    list_filter = ('etapa', 'prioridad', 'tramite_tipo', 'fecha_vencimiento')
    date_hierarchy = 'fecha_recepcion'

admin.site.register(Tramite, TramiteAdmin)
