# RECETARIO DE INICIALIZACIÓN DE UNA APLICACIÓN EN DJANGO PARA MAC

1. Para realizar la instalación de Django

- Crear una nueva carpeta en Documentos o Escritorio
- Abrir Terminal y navegar a la carpeta creada
- Crear el ambiente virtual para aislar las dependencias:
  ```
  python3 -m venv myvenv
  ```
- Activar el ambiente virtual:
  ```
  source myvenv/bin/activate
  ```
- Actualizar pip:
  ```
  python3 -m pip install --upgrade pip
  ```
- Crear el archivo requirements.txt al lado de myvenv y agregar "Django==4.1.2"
- Instalar las dependencias:
  ```
  pip install -r requirements.txt
  ```
- Crear un nuevo proyecto Django:
  ```
  django-admin startproject instituto
  ```
- Entrar a la carpeta del proyecto:
  ```
  cd instituto
  ```
- Copiar requirements.txt dentro de la carpeta instituto
- Abrir el proyecto con un editor de código (como Visual Studio Code)
- Crear un archivo .gitignore con el siguiente contenido:
  ```
  /myvenv
  *.pyc
  __pycache__
  db.sqlite3
  ```
- Crear un nuevo repositorio en GitHub
- Inicializar Git y hacer el primer commit:
  ```
  git init
  git add .
  git commit -m "Primer commit"
  git branch -M main
  git remote add origin <URL_DEL_REPOSITORIO>
  git push -u origin main
  ```
- Ejecutar el servidor de desarrollo:
  ```
  python3 manage.py runserver
  ```

2. Al clonar el repositorio en otro Mac

- Clonar el repositorio
- Crear y activar el ambiente virtual:
  ```
  python3 -m venv myvenv
  source myvenv/bin/activate
  ```
- Instalar las dependencias:
  ```
  pip install -r requirements.txt
  ```
- Ejecutar el servidor:
  ```
  python3 manage.py runserver
  ```

3. Agregando una nueva aplicación

- En la carpeta del proyecto:
  ```
  python3 manage.py startapp alumnos
  ```
- En settings.py, agregar 'alumnos' al final de INSTALLED_APPS
- En urls.py del proyecto, agregar:
  ```python
  from django.urls import path, include
  
  urlpatterns = [
      # ... otras urls
      path('alumnos/', include('alumnos.urls')),
  ]
  ```
- Crear urls.py en la carpeta de la app 'alumnos'

4. Agregando un template

- En la app, crear carpetas: templates/alumnos
- Agregar archivo HTML (por ejemplo, index.html)
- En views.py de la app:
  ```python
  def index(request):
      context = {}
      return render(request, 'alumnos/index.html', context)
  ```

5. Mapeando modelos

- En models.py de la app, definir modelos
- Realizar migraciones:
  ```
  python3 manage.py makemigrations
  python3 manage.py migrate
  ```
- Crear superusuario:
  ```
  python3 manage.py createsuperuser
  ```
- Registrar modelos en admin.py

6. Usando modelos en views y templates

- En views.py, importar modelos y usarlos en las funciones de vista
- En templates, usar el contexto pasado desde las vistas

7. Trabajando con múltiples modelos

- En views.py, consultar múltiples modelos y pasarlos en el contexto
- En templates, iterar sobre las colecciones de objetos

8. Referenciando modelos entre aplicaciones

- Importar modelos de otras apps en views.py:
  ```python
  from otraapp.models import ModeloDeOtraApp
  ```

9. Configurando rutas generales del proyecto

- Crear una app para navegación general
- Definir vistas en views.py de esta app
- En urls.py del proyecto, agregar rutas generales

10. Usando un template base

- Crear base.html en una app de navegación o en la raíz del proyecto
- Usar {% extends "ruta/a/base.html" %} en otros templates
- Definir bloques en base.html y sobrescribirlos en templates hijos

Nota: En Mac, no es necesario preocuparse por problemas de permisos de ejecución de scripts como en Windows.
