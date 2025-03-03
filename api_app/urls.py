# Importa la función path del módulo de URLs de Django
from django.urls import path
# Importa las vistas desde el módulo views de la aplicación actual
from .views import (
    PersonaList, PersonaByDocumento, ActualizarPersona,
    TareaList, TareaByFecha, TareaByRangoFechas, TareaByPersona
)

# Define la lista de patrones de URL para la aplicación 'api_app'
urlpatterns = [
    # Rutas para la gestión de personas
    # Lista de personas
    path('personas/', PersonaList.as_view(), name='persona-list'),
    # Crear una nueva persona
    path('personas/crear/', PersonaList.as_view(), name='persona-crear'),
    # Actualizar una persona existente por su ID (pk)
    path('personas/actualizar/<int:pk>/', ActualizarPersona.as_view(), name='persona-actualizar'),
    # Obtener una persona por su documento
    path('personas/documento/<str:documento>/', PersonaByDocumento.as_view(), name='persona-por-documento'),

    # Rutas para la gestión de tareas
    # Lista de tareas
    path('tareas/', TareaList.as_view(), name='tarea-list'),
    # Crear una nueva tarea
    path('tareas/crear/', TareaList.as_view(), name='tarea-crear'),
    # Obtener tareas por fecha específica
    path('tareas/fecha/<str:fecha>/', TareaByFecha.as_view(), name='tareas-por-fecha'),
    # Obtener tareas por un rango de fechas
    path('tareas/rango/', TareaByRangoFechas.as_view(), name='tareas-por-rango-fechas'),
    # Obtener tareas asignadas a una persona específica
    path('tareas/persona/', TareaByPersona.as_view(), name='tareas-por-persona'),
]