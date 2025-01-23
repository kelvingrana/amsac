from django import forms
from .models import Tramite, Usuario, Etapa
from django.utils import timezone
from .models import Tramite
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario


# formulario para que los usuarios creen un nuevo trámite.

class TramiteForm(forms.ModelForm):
    class Meta:
        model = Tramite
        fields = ['no_oficio', 'fecha_recepcion', 'fecha_vencimiento', 'prioridad', 'tramite_tipo', 'receptor_responsable','inspector_responsable', 'etapa', 'comentarios']
        widgets = {
            'fecha_recepcion': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_vencimiento': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

# Formulario de busqueda por empleado
# ----------------------------------------------------------------------------------------

class FiltroTramitesForm(forms.Form):
    TIPO_BUSQUEDA_CHOICES = [
        ('', 'Seleccione el tipo de búsqueda'),
        ('receptor', 'Recepcionista'),
        ('inspector', 'Inspector'),
        ('resolutor', 'Resultor'),
        ('lider_proyecto', 'Líder de Proyecto'),
        ('sub_lider_proyecto', 'Sub Líder de Proyecto'),
        ('resultor_proyecto', 'Resultor de Proyecto'),
    ]

    empleado_choices = [(usuario.id, usuario.username) for usuario in Usuario.objects.all()]
    
    tipo_busqueda = forms.ChoiceField(choices=TIPO_BUSQUEDA_CHOICES, required=False, label='Tipo de Búsqueda')
    empleado = forms.ChoiceField(choices=[('', 'Seleccione un empleado')] + empleado_choices, required=False, label='Empleado Responsable')
    fecha_inicio = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label='Fecha Inicio')
    fecha_fin = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False, label='Fecha Fin')

    def filter_tramites(self, queryset):
        # Filtrar por tipo de búsqueda y empleado
        tipo_busqueda = self.cleaned_data.get('tipo_busqueda')
        empleado_id = self.cleaned_data.get('empleado')
        
        if tipo_busqueda and empleado_id:
            if tipo_busqueda == 'receptor':
                queryset = queryset.filter(receptor_responsable_id=empleado_id)
            elif tipo_busqueda == 'inspector':
                queryset = queryset.filter(inspector_responsable_id=empleado_id)
            elif tipo_busqueda == 'resolutor':
                queryset = queryset.filter(resultor_responsable_id=empleado_id) 
            elif tipo_busqueda == 'lider_proyecto':
                queryset = queryset.filter(lider_proyecto_id=empleado_id)
            elif tipo_busqueda == 'sub_lider_proyecto':
                queryset = queryset.filter(sub_lider_proyecto_id=empleado_id)
            elif tipo_busqueda == 'resultor_proyecto':
                queryset = queryset.filter(resultor_proyecto_id=empleado_id)
                
        
        # Filtrar por fechas
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        fecha_fin = self.cleaned_data.get('fecha_fin')
        
        if fecha_inicio:
            queryset = queryset.filter(fecha_vencimiento__gte=fecha_inicio)
        if fecha_fin:
            queryset = queryset.filter(fecha_vencimiento__lte=fecha_fin)
        
        return queryset

# Formulario para cambiar de estado (etapa)
# ----------------------------------------------------------------------------------------
class MoverTramiteForm(forms.Form):
    nueva_etapa = forms.ModelChoiceField(queryset=Etapa.objects.all(), label="Nueva Etapa")

# Formulario para elegir un archivo excel   
# ----------------------------------------------------------------------------------------


class ImportTramiteForm(forms.Form):
    excel_file = forms.FileField(label="Seleccionar archivo Excel")

    def clean_excel_file(self):
        excel_file = self.cleaned_data.get('excel_file')

        # Validación del tipo de archivo, debe ser Excel
        if not excel_file.name.endswith('.xlsx') and not excel_file.name.endswith('.xls'):
            raise forms.ValidationError("El archivo debe ser de tipo Excel (.xlsx o .xls)")

        return excel_file


# Formulario personalizado para crear usuarios

class CustomUserCreationForm(UserCreationForm):
    rol = forms.ChoiceField(choices=Usuario.ROLES, required=True, label='Rol')

    class Meta:
        model = Usuario
        fields = ['username', 'email', 'rol', 'password1', 'password2']
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }