"""
URL configuration for api_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Importa el módulo de administración de Django
from django.contrib import admin
# Importa las funciones path e include del módulo de URLs de Django
from django.urls import path, include

# Define la lista de patrones de URL para el proyecto
urlpatterns = [
    # Ruta para la interfaz de administración de Django
    path('admin/', admin.site.urls),
    # Incluye las URLs definidas en el archivo urls.py de la aplicación 'api_app'
    path('api/', include('api_app.urls')),
]