from django.test import TestCase
from rest_framework.test import APITestCase # Clase de pruebas para la API
from rest_framework import status
from .models import Persona, Tarea # Importa los modelos de la aplicación
from datetime import date

# Clase para probar la api relacionada con personas

class PersonasApiTestCase(APITestCase):
    def setUp(self):
        # crear la instancia de una persona para las pruebas
        self.persona = Persona.objects.create(
            nombre  = 'Prueba persona',
            apellido = 'Test',
            documento = '10798465',
            email = 'prueba.test@gmail.com',
            activo = True
        )

    def test_list_personas(self):
        response = self.client.get('/api/personas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)

    def test_create_persona(self):
        data = {
            'nombre'  : 'Maria',
            'apellido' : 'Rodriguez',
            'documento' : '5566778899',
            'email' : 'maria.rodriguez@gmail.com',
            'activo' : True
        }
        # Realizar la solicitud http post al api
        response = self.client.post('/api/personas/crear/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['nombre'], "Maria")

class TareasApiTestCase(APITestCase):
    def setUp(self):
        # crear la instancia de una persona para las pruebas
        self.persona = Persona.objects.create(
            nombre="Luis",
            apellido="Martínez",
            documento="2233445566",
            email="luis.martinez@gmail.com",
            activo=True
        )
        # Instanciar una tarea para el test
        self.tarea = Tarea.objects.create(
            titulo="Tarea de prueba",
            descripcion="Descripción de la tarea de prueba",
            fecha_limite=date(2025, 10, 1),
            persona=self.persona # Relacion con la persona creada
        )

    def test_list_tareas(self):
        response = self.client.get('/api/tareas/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        print("Response Tarea", response.data['data'])

    def test_create_tarea(self):
        data = {
            'titulo'  : 'Nueva Tarea',
            'descripcion' : 'Descripción de la nueva tarea',
            'fecha_limite' : '2025-10-01',
            'persona' : self.persona.id_persona # Relacion con la persona creada
        }
        # Realizar la solicitud http post al api
        response = self.client.post('/api/tareas/crear/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['titulo'], "Nueva Tarea")
        print("Response Creacion Tarea", response.data['titulo'])