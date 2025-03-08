# API Project

Este es un proyecto Django que proporciona una API para gestionar personas y tareas.

## Requisitos

- Python 3.11
- Django 5.1.6
- Django REST Framework 3.15.2
- PostgreSQL
- Otros requisitos están listados en el archivo `requirements.txt`

## Instalación

1. Clona el repositorio:
    ```sh
    git clone <URL_DEL_REPOSITORIO>
    cd api_project
    ```

2. Crea y activa un entorno virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # En Windows usa `venv\Scripts\activate`
    ```

3. Instala las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configura la base de datos PostgreSQL en el archivo `api_project/settings.py`:
    ```python
    DATABASES = {
        'default': {
           Agregar las credenciales de la base de datos
        }
    }
    ```

5. Realiza las migraciones de la base de datos:
    ```sh
    python manage.py migrate
    ```

6. Crea un superusuario para acceder a la interfaz de administración:
    ```sh
    python manage.py createsuperuser
    ```

7. Inicia el servidor de desarrollo:
    ```sh
    python manage.py runserver
    ```

## Uso

### Endpoints de Personas

- Listar todas las personas: `GET /api/personas/`
- Crear una nueva persona: `POST /api/personas/crear/`
- Actualizar una persona: `PUT /api/personas/actualizar/<int:pk>/`
- Obtener una persona por documento: `GET /api/personas/documento/<str:documento>/`

### Endpoints de Tareas

- Listar todas las tareas: `GET /api/tareas/`
- Crear una nueva tarea: `POST /api/tareas/crear/`
- Actualizar una tarea: `PUT /api/tareas/actualizar/<int:pk>/`
- Obtener tareas por fecha: `GET /api/tareas/fecha/<str:fecha>/`
- Obtener tareas por rango de fechas: `GET /api/tareas/rango/?fecha_inicio=<fecha>&fecha_fin=<fecha>`
- Obtener tareas por persona: `GET /api/tareas/persona/?documento=<documento>`

## Contribuir

1. Haz un fork del proyecto.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT.