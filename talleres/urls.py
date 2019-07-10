from django.urls import path, include
from talleres import views as core_views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('', include('social_django.urls', namespace='social')),
    path('login/', views.cargarLogin, name='cargarLogin'),
    path('registro/', core_views.signup, name='signup'),
    path('talleres',views.talleres, name='talleres'),
    path('administrarTalleres', views.administrarTalleres, name='administrarTalleres'),
    path('agregarTaller', views.agregarTaller, name='agregarTaller'),
    path('guardarTaller', views.guardarTaller, name='guardarTaller'),
    path('modificarTaller/<int:taller_codigo>', views.modificarTaller, name='modificarTaller'),
    path('tallerModificado', views.tallerModificado, name='tallerModificado'),
    path('eliminarTaller/<int:taller_codigo>', views.eliminarTaller, name='eliminarTaller'),
    path('propuestas',views.cargarPropuestas, name='cargarPropuestas'),
    path('politica',views.cargarPolitica,name='cargarPolitica'),
    path('propuesta/<int:propuesta_id>', views.detallePropuestas, name='propuestaD'),
    path('propuvoto/<int:propuesta_id>', views.VotosUp, name='votosUp'),
    path('propunovoto/<int:propuesta_id>', views.VotosDown, name='votosDown'),
    path('agregarPropuesta', views.agregarNuevaPropuesta, name='agregarNuevaPropuesta'),
    path('guardarPropuesta', views.guardarNuevaPropuesta, name='guardarNuevaPropuesta'),
    path('propuestasParaAprobar', views.propuestasParaAprobar, name='propuestasParaAprobar'),
    path('confirmarPropuestaParaAprobar/<int:propuesta_id>', views.confirmarPropuestaParaAprobar, name='confirmarPropuestaParaAprobar'),
    path('guardarPropuestaAprobada/<int:propuesta_id>', views.guardarPropuestaAprobada, name='guardarPropuestaAprobada'),
    path('confirmarEliminarPropuestaParaAprobar/<int:propuesta_id>', views.confirmarEliminarPropuestaParaAprobar, name='confirmarEliminarPropuestaParaAprobar'),
    path('eliminarPropuestaParaAprobar/<int:propuesta_id>', views.eliminarPropuestaParaAprobar, name='eliminarPropuestaParaAprobar'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)