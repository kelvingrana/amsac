from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from datetime import timedelta

# Modelo personalizado para usuarios
class Usuario(AbstractUser):
    ROLES = [
        ('recepcionista', 'Recepcionista'),
        ('inspector', 'Inspector'),
        ('resultor', 'Resultor'),
        ('lider_proyecto', 'Líder de Proyecto'),
        ('sub_lider_proyecto', 'Sub Líder de Proyecto'),
        ('resultor_proyecto', 'Resultor de Proyecto'),
    ]
    rol = models.CharField(max_length=20, choices=ROLES, null=True, blank=True) 
    
    def __str__(self):
        return f"{self.username}"  # Para mostrar el rol del usuario agregar ({self.get_rol_display()})


# Modelo para la etapa de un trámite
class Etapa(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Modelo para los trámites
class Tramite(models.Model):
    ESTADO_CHOICES = [
        ('Recepción', 'Recepción'),
        ('Inspección', 'Inspección'),
        ('Resolución', 'Resolución'),
        ('Finalizado', 'Finalizado'),
        ('Pendiente Subsano', 'Pendiente Subsano'),
        ('Inspección Proyecto', 'Inspección Proyecto'),
        ('Resolución Proyecto', 'Resolución Proyecto'),
    ]

    # Información del trámite
    no_oficio = models.CharField(max_length=50)
    fecha_recepcion = models.DateTimeField()
    fecha_vencimiento = models.DateTimeField()
    prioridad = models.CharField(max_length=10, choices=[('alta', 'Alta'), ('media', 'Media'), ('baja', 'Baja')])
    tramite_tipo = models.CharField(max_length=20, choices=[('inscripcion', 'Inscripción'), ('desmembracion', 'Desmembración'),
                                                            ('consolidacion', 'Consolidación'), ('comprobante', 'Comprobante')])
    receptor_responsable = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='receptor_responsable')                                                       
    inspector_responsable = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='inspector_responsable')
    resultor_responsable = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='resultor_responsable')
    lider_proyecto = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='lider_proyecto')
    sub_lider_proyecto = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_lider_proyecto')
    resultor_proyecto = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='resultor_proyecto')

    etapa = models.ForeignKey(Etapa, on_delete=models.CASCADE)
    fecha_movimiento = models.DateTimeField(auto_now=True)  # Fecha en que el trámite cambia de etapa
    comentarios = models.TextField(blank=True, null=True)
    delegado_a = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, related_name='delegado_a')
    
    def __str__(self):
        return f"Trámite {self.no_oficio} - {self.etapa.nombre}"
    
    def get_estado(self):
        if self.fecha_vencimiento <= self.fecha_movimiento:
            return 'Vencido'
        elif self.fecha_vencimiento - self.fecha_movimiento <= timedelta(days=2):
            return 'Por Vencer'
        return 'Ok'

