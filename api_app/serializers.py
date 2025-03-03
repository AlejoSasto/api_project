# Importa el módulo serializers del framework Django REST
from rest_framework import serializers
# Importa los modelos Persona y Tarea desde el módulo models de la aplicación actual
from .models import Persona, Tarea

# Define el serializador para el modelo Persona
class PersonaSerializer(serializers.ModelSerializer):
    # Meta clase para especificar el modelo y los campos a incluir en el serializador
    class Meta:
        model = Persona
        fields = '__all__'  # Incluye todos los campos del modelo Persona

# Define el serializador para el modelo Tarea
class TareaSerializer(serializers.ModelSerializer):
    # Meta clase para especificar el modelo y los campos a incluir en el serializador
    class Meta:
        model = Tarea
        fields = '__all__'  # Incluye todos los campos del modelo Tarea