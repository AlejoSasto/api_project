# Importa el módulo models de Django para definir los modelos de la base de datos
from django.db import models

# Define el modelo Persona
class Persona(models.Model):
    # Campo de clave primaria autoincremental
    id_persona = models.AutoField(primary_key=True, editable=False, db_column='T001IdPersona')
    # Campo de nombre con un máximo de 100 caracteres
    nombre = models.CharField(max_length=100, db_column='T001Nombre')
    # Campo de apellido con un máximo de 100 caracteres
    apellido = models.CharField(max_length=100, db_column='T001Apellido')
    # Campo de documento único con un máximo de 20 caracteres
    documento = models.CharField(max_length=20, unique=True, db_column='T001Documento')
    # Campo de email único
    email = models.EmailField(unique=True, db_column='T001Email')
    # Campo booleano para indicar si la persona está activa
    activo = models.BooleanField(default=True, db_column='T001Activo')

    # Método para representar el objeto como una cadena
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    # Meta clase para especificar opciones del modelo
    class Meta:
        db_table = 'T001Persona'  # Nombre de la tabla en la base de datos
        verbose_name = 'Persona'  # Nombre singular del modelo
        verbose_name_plural = 'Personas'  # Nombre plural del modelo

# Define el modelo Tarea
class Tarea(models.Model):
    # Campo de clave primaria autoincremental
    id_tarea = models.AutoField(primary_key=True, editable=False, db_column='T002IdTarea')
    # Campo de título con un máximo de 200 caracteres
    titulo = models.CharField(max_length=200, db_column='T002Titulo')
    # Campo de descripción de texto largo
    descripcion = models.TextField(db_column='T002Descripcion')
    # Campo de fecha límite
    fecha_limite = models.DateField(db_column='T002FechaLimite')
    # Campo de clave foránea que referencia a Persona
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE, related_name='tareas', db_column='T002PersonaId')

    # Método para representar el objeto como una cadena
    def __str__(self):
        return self.titulo

    # Meta clase para especificar opciones del modelo
    class Meta:
        db_table = 'T002Tarea'  # Nombre de la tabla en la base de datos
        verbose_name = 'Tarea'  # Nombre singular del modelo
        verbose_name_plural = 'Tareas'  # Nombre plural del modelo