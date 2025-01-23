from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('login_amsac/', views.login_amsac, name='login_amsac'),
    path('logout_amsac/', views.logout_amsac, name='logout_amsac'),
    path('crear_tramite/', views.crear_tramite, name='crear_tramite'),
    path('bandeja_inspeccion/', views.bandeja_inspeccion, name='bandeja_inspeccion'),
    path('bandeja_recepcion/', views.bandeja_recepcion, name='bandeja_recepcion'),
    path('bandeja_resolucion/', views.bandeja_resolucion, name='bandeja_resolucion'),
    path('bandeja_cola_notificacion/', views.bandeja_cola_notificacion, name='bandeja_cola_notificacion'),
    path('bandeja_finalizados/', views.bandeja_finalizados, name='bandeja_finalizados'),
    path('bandeja_inspeccion_proyectos/', views.bandeja_inspeccion_proyectos, name='bandeja_inspeccion_proyectos'),
    path('cambiar_etapa/<int:tramite_id>/', views.cambiar_etapa, name='cambiar_etapa'),
    path('import_tramites/', views.import_tramites, name='import_tramites'),
    path('export_tramites/', views.export_tramites, name='export_tramites'),
    path('bandeja_resolucion_proyectos/', views.bandeja_resolucion_proyectos, name='bandeja_resolucion_proyectos'),
    
]
