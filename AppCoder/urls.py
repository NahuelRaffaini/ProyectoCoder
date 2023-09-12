from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="Inicio"),
    path('listaCursos/', CursoList.as_view(), name="ListarCursos"),
    path('detalleCurso/<pk>', CursoDetail.as_view(), name="DetalleCurso"),
    path('creaCurso/', CursoCreate.as_view(), name="CrearCurso"),
    path('actualizarCurso/<pk>', CursoUpdate.as_view(), name="ActualizarCurso"),
    path('eliminarCurso/<pk>', CursoDelete.as_view(), name="EliminarCurso"),
    path('listaProfe/', ProfesorList.as_view(), name="ListarProfe"),
    path('detalleProfe/<pk>', ProfesorDetail.as_view(), name="DetalleProfe"),
    path('creaProfe/', ProfesorCreate.as_view(), name="CrearProfe"),
    path('actualizarProfe/<pk>', ProfesorUpdate.as_view(), name="ActualizarProfe"),
    path('eliminarProfe/<pk>', ProfesorDelete.as_view(), name="EliminarProfe"),
    path('listaEstu/', EstudianteList.as_view(), name="ListarEstu"),
    path('detalleEstu/<pk>', EstudianteDetail.as_view(), name="DetalleEstu"),
    path('creaEstu/', EstudianteCreate.as_view(), name="CrearEstu"),
    path('actualizarEstu/<pk>', EstudianteUpdate.as_view(), name="ActualizarEstu"),
    path('eliminarEstu/<pk>', EstudianteDelete.as_view(), name="EliminarEstu"),
    path('filtrar-estudiantes/', filtrar_estudiantes, name='filtrar_estudiantes'),
    path('filtrar-cursos/', filtrar_cursos, name='filtrar_cursos'),
    path('filtrar-profesores/', filtrar_profesores, name='filtrar_profesores')
]
