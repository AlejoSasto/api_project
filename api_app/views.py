# Importaciones necesarias para las vistas de Django y Django REST Framework
from django.shortcuts import get_object_or_404  # Importa una función para obtener un objeto o devolver un error 404 si no se encuentra
from rest_framework.response import Response  # Importa la clase Response para devolver respuestas HTTP
from rest_framework import generics, status  # Importa clases genéricas y códigos de estado HTTP
from rest_framework.exceptions import NotFound, ValidationError  # Importa excepciones para manejar errores específicos
from .models import Persona, Tarea  # Importa los modelos Persona y Tarea
from .serializers import PersonaSerializer, TareaSerializer  # Importa los serializadores para los modelos Persona y Tarea

# ---------------------------------------- CRUD Personas ----------------------------------------

# Vista para listar
class PersonaList(generics.ListCreateAPIView):
    queryset = Persona.objects.all()  # Define el conjunto de consultas para obtener todas las personas
    serializer_class = PersonaSerializer  # Define el serializador a utilizar

    # Método GET para listar todas las personas
    def get(self, request):
        personas = Persona.objects.all()  # Obtiene todas las personas
        serializer = PersonaSerializer(personas, many=True)  # Serializa las personas
        if not personas:
            raise NotFound('No se encontraron personas.')  # Lanza una excepción si no se encuentran personas
        return Response({'success': True, 'detail': 'Listado de personas.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos serializados
# Vista listar personas por id

class PersonaListId(generics.ListCreateAPIView):
    queryset = Persona.objects.all()  # Define el conjunto de consultas para obtener todas las personas
    serializer_class = PersonaSerializer  # Define el serializador a utilizar

    # Método GET para listar todas las personas
    def get(self, request, pk):
        personas = Persona.objects.filter(id=pk)  # Obtiene todas las personas
        serializer = PersonaSerializer(personas, many=True)  # Serializa las personas
        if not personas:
            raise NotFound('No se encontraron personas.')  # Lanza una excepción si no se encuentran personas
        return Response({'success': True, 'detail': 'Listado de personas.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos serializados
    
# Vista específica para crear personas
class CrearPersona(generics.CreateAPIView):
    queryset = Persona.objects.all()  # Define el conjunto de consultas para obtener todas las personas
    serializer_class = PersonaSerializer  # Define el serializador a utilizar

    # Método POST para crear una nueva persona
    def post(self, request):
        serializer = PersonaSerializer(data=request.data)  # Serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        serializer.save()  # Guarda la nueva persona
        return Response({'success': True, 'detail': 'Persona creada correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)  # Devuelve una respuesta con los datos de la nueva persona

# Vista para actualizar personas
class ActualizarPersona(generics.UpdateAPIView):
    queryset = Persona.objects.all()  # Define el conjunto de consultas para obtener todas las personas
    serializer_class = PersonaSerializer  # Define el serializador a utilizar

    # Método PUT para actualizar una persona existente
    def put(self, request, pk):
        persona = get_object_or_404(Persona, pk=pk)  # Obtiene la persona o devuelve un error 404 si no se encuentra
        email = request.data.get('email', None)  # Obtiene el email de los datos de la solicitud
        
        # Verificar si el email ha cambiado
        if email and email != persona.email:
            # Verificar si ya existe otra persona con el mismo email
            if Persona.objects.filter(email=email).exclude(pk=pk).exists():
                return Response({'email': ['Persona with this email already exists.']}, status=status.HTTP_400_BAD_REQUEST)  # Devuelve un error si el email ya existe
        
        serializer = PersonaSerializer(persona, data=request.data)  # Serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        serializer.save()  # Guarda la persona actualizada
        return Response({'success': True, 'detail': 'Persona actualizada correctamente.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos de la persona actualizada

# Vista para buscar una persona por documento
class PersonaByDocumento(generics.ListAPIView):
    serializer_class = PersonaSerializer  # Define el serializador a utilizar

    # Método GET para obtener una persona por su documento
    def get(self, request, documento):
        persona = Persona.objects.filter(documento=documento).first()  # Busca la persona por su documento
        if not persona:
            raise NotFound('No se encontró una persona con ese documento.')  # Lanza una excepción si no se encuentra la persona
        serializer = PersonaSerializer(persona)  # Serializa la persona
        return Response({'success': True, 'detail': 'Persona encontrada.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos de la persona

# ---------------------------------------- CRUD Tareas ----------------------------------------

# Vista para listar y crear tareas
class TareaList(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()  # Define el conjunto de consultas para obtener todas las tareas
    serializer_class = TareaSerializer  # Define el serializador a utilizar

    # Método GET para listar todas las tareas
    def get(self, request):
        tareas = Tarea.objects.all()  # Obtiene todas las tareas
        serializer = TareaSerializer(tareas, many=True)  # Serializa las tareas
        if not tareas:
            raise NotFound('No se encontraron tareas.')  # Lanza una excepción si no se encuentran tareas
        return Response({'success': True, 'detail': 'Listado de tareas.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos serializados

# Vista específica para crear tareas
class CrearTarea(generics.CreateAPIView):
    queryset = Tarea.objects.all()  # Define el conjunto de consultas para obtener todas las tareas
    serializer_class = TareaSerializer  # Define el serializador a utilizar

    # Método POST para crear una nueva tarea
    def post(self, request):
        serializer = TareaSerializer(data=request.data)  # Serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        serializer.save()  # Guarda la nueva tarea
        return Response({'success': True, 'detail': 'Tarea creada correctamente.', 'data': serializer.data}, status=status.HTTP_201_CREATED)  # Devuelve una respuesta con los datos de la nueva tarea

# Vista para actualizar tareas
class ActualizarTarea(generics.UpdateAPIView):
    queryset = Tarea.objects.all()  # Define el conjunto de consultas para obtener todas las tareas
    serializer_class = TareaSerializer  # Define el serializador a utilizar

    # Método PUT para actualizar una tarea existente
    def put(self, request, pk):
        tarea = get_object_or_404(Tarea, pk=pk)  # Obtiene la tarea o devuelve un error 404 si no se encuentra
        serializer = TareaSerializer(tarea, data=request.data)  # Serializa los datos de la solicitud
        serializer.is_valid(raise_exception=True)  # Valida los datos y lanza una excepción si no son válidos
        serializer.save()  # Guarda la tarea actualizada
        return Response({'success': True, 'detail': 'Tarea actualizada correctamente.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos de la tarea actualizada

# Vista para buscar tareas por fecha límite
class TareaByFecha(generics.ListAPIView):
    serializer_class = TareaSerializer  # Define el serializador a utilizar

    # Método GET para obtener tareas por fecha límite
    def get(self, request, fecha):
        tareas = Tarea.objects.filter(fecha_limite=fecha)  # Busca las tareas por fecha límite
        if not tareas:
            raise NotFound('No se encontraron tareas para la fecha especificada.')  # Lanza una excepción si no se encuentran tareas
        serializer = TareaSerializer(tareas, many=True)  # Serializa las tareas
        return Response({'success': True, 'detail': 'Listado de tareas para la fecha.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos de las tareas

# Vista para buscar tareas por rango de fechas
class TareaByRangoFechas(generics.ListAPIView):
    serializer_class = TareaSerializer  # Define el serializador a utilizar

    # Método GET para obtener tareas por un rango de fechas
    def get(self, request):
        fecha_inicio = request.query_params.get('fecha_inicio')  # Obtiene la fecha de inicio de los parámetros de la solicitud
        fecha_fin = request.query_params.get('fecha_fin')  # Obtiene la fecha de fin de los parámetros de la solicitud
        if not fecha_inicio or not fecha_fin:
            raise ValidationError('Debe proporcionar fecha_inicio y fecha_fin.')  # Lanza una excepción si no se proporcionan ambas fechas
        tareas = Tarea.objects.filter(fecha_limite__range=[fecha_inicio, fecha_fin])  # Busca las tareas en el rango de fechas
        serializer = TareaSerializer(tareas, many=True)  # Serializa las tareas
        return Response({'success': True, 'detail': 'Listado de tareas en el rango de fechas.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos de las tareas

# Vista para buscar tareas por persona
class TareaByPersona(generics.ListAPIView):
    serializer_class = TareaSerializer  # Define el serializador a utilizar

    # Método GET para obtener tareas por el documento de una persona
    def get(self, request):
        documento = request.query_params.get('documento')  # Obtiene el documento de los parámetros de la solicitud
        if not documento:
            raise ValidationError('Debe proporcionar un documento de persona.')  # Lanza una excepción si no se proporciona el documento
        tareas = Tarea.objects.filter(persona__documento=documento)  # Busca las tareas por el documento de la persona
        if not tareas:
            raise NotFound('No se encontraron tareas para esta persona.')  # Lanza una excepción si no se encuentran tareas
        serializer = TareaSerializer(tareas, many=True)  # Serializa las tareas
        return Response({'success': True, 'detail': 'Listado de tareas de la persona.', 'data': serializer.data}, status=status.HTTP_200_OK)  # Devuelve una respuesta con los datos de las tareas