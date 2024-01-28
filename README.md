
# Instrucciones de Instalación del Proyecto

Antes de comenzar, asegúrate de tener conocimientos básicos en la creación de instancias en EC2 de AWS, así como en conexiones SSH o Putty y transferencia de archivos por FTP.

## Pasos para la Instalación

### 1. Crear una Instancia EC2 en AWS
Visita [Bitnami Django Stack en AWS](https://bitnami.com/stack/django/cloud/aws) para instalar Django. Selecciona la opción de "Single Tier" e inicia sesión con tu cuenta de AWS.

### 2. Configuración de la Instancia
Durante la configuración en AWS, genera una llave `.ppk` para futuros accesos vía SSH o FTP y la transferencia de archivos.

### 3. Conexión SSH
Utiliza Putty o una herramienta similar con tu llave `.ppk` para acceder a tu instancia. Ejecuta los siguientes comandos para preparar el entorno del proyecto:
```bash
cd /opt/bitnami/projects/
django-admin startproject PROJECT_NAME
```
Reemplaza `PROJECT_NAME` con el nombre de tu proyecto.

# 4. Transferencia FTP
Accede vía FTP a `/opt/bitnami/projects/PROJECT_NAME` y sube tu proyecto.

# 5. Configuraciones y Migraciones
Vuelve a SSH y ejecuta:
```bash
cd /opt/bitnami/projects/PROJECT_NAME
sudo python manage.py migrate
sudo python manage.py makemigrations
sudo python -m pip install Pillow
```

# 6. Crea el Superusuario
```bash
python manage.py createsuperuser
```
Sigue las instrucciones para crear un superusuario.

# 7. Detén Apache
```bash
sudo /opt/bitnami/ctlscript.sh stop apache
```
Esto libera el puerto 80.

# 8. Configura `ALLOWED_HOSTS`
Edita `settings.py` para incluir tu IP externa de EC2 en `ALLOWED_HOSTS`:
```python
ALLOWED_HOSTS = ['35.153.181.103']
```

# 9. Iniciar el Servidor
Desde la carpeta del proyecto, inicia el servidor:
```bash
nohup sudo python manage.py runserver 0.0.0.0:80 &
```

Ahora tu proyecto debería estar accesible en `http://35.153.181.103/admin`.

```

Asegúrate de reemplazar `PROJECT_NAME` con el nombre real de tu proyecto Django y `35.153.181.103` con la IP pública de tu instancia EC2.