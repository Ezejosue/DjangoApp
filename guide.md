
# Guía para Crear una App con Django

Esta guía proporciona un resumen paso a paso para crear una aplicación con Django, desde la configuración inicial hasta ejecutar el servidor de desarrollo.

## Configuración Inicial

### 1. Instalar Django

Primero, asegúrate de tener Python instalado. Luego, instala Django utilizando pip:

```bash
pip install django
```

### 2. Crear un Entorno Virtual

Es recomendable usar un entorno virtual para manejar las dependencias de tu proyecto:

```bash
python -m venv mi_entorno
```

Activar el entorno virtual:

- En Windows:
  ```bash
  mi_entorno\Scripts\activate
  ```

- En macOS y Linux:
  ```bash
  source mi_entorno/bin/activate
  ```

## Crear un Proyecto Django

### 3. Crear un Nuevo Proyecto

Con Django instalado y el entorno virtual activo, crea un nuevo proyecto:

```bash
django-admin startproject mi_proyecto
```

### 4. Navegar al Directorio del Proyecto

```bash
cd mi_proyecto
```

## Crear una App Django

### 5. Crear una Nueva App

```bash
python manage.py startapp mi_app
```

## Configurar la App

### 6. Añadir la App a INSTALLED_APPS

En `mi_proyecto/settings.py`, añade tu app a `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'mi_app',
]
```

## Modelos y Migraciones

### 7. Definir Modelos (Opcional)

Define tus modelos en `mi_app/models.py` si tu app los necesita.

### 8. Realizar Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

## Crear un Superusuario

### 9. Crear un Superusuario

```bash
python manage.py createsuperuser
```

## Ejecutar el Servidor de Desarrollo

### 10. Iniciar el Servidor de Desarrollo

```bash
python manage.py runserver
```

Visita `http://127.0.0.1:8000/` en tu navegador para ver tu nuevo sitio Django.

---

Con estos pasos, tienes una base sólida para comenzar el desarrollo de tu aplicación Django.
