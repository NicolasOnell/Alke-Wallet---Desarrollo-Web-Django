# Alke Wallet - Billetera Digital

## Descripción del Proyecto

**Alke Wallet** es una aplicación web desarrollada con Django que permite a los usuarios gestionar y administrar sus activos financieros de forma segura y sencilla. El proyecto aborda desafíos relacionados con el acceso y gestión de datos, creación de modelos robustos, sincronización mediante migraciones, ejecución de consultas personalizadas e implementación de operaciones CRUD.

### Objetivo Principal

Desarrollar una aplicación web funcional que permita a los usuarios:
- Crear y gestionar sus cuentas digitales
- Realizar transacciones entre cuentas
- Consultar saldos
- Generar reportes de transacciones

## Tecnologías Utilizadas

- **Backend:** Django 6.0.4
- **Base de Datos:** SQLite (desarrollo), PostgreSQL (producción)
- **Python:** 3.x
- **ORM:** Django ORM
- **Frontend:** HTML5 + CSS3
- **Control de Versiones:** Git

## Estructura del Proyecto

```
websolutions_platform/
├── manage.py                      # Script de administración de Django
├── db.sqlite3                    # Base de datos SQLite
├── websolutions_platform/        # Configuración del proyecto
│   ├── settings.py              # Configuraciones del proyecto
│   ├── urls.py                  # Rutas principales
│   ├── wsgi.py                  # Configuración WSGI
│   └── asgi.py                  # Configuración ASGI
├── gestion/                      # Aplicación principal
│   ├── models.py                # Modelos de datos (Cliente, Cuenta, Transacción, etc.)
│   ├── views.py                 # Vistas basadas en clases (CRUD)
│   ├── urls.py                  # Rutas de la aplicación
│   ├── admin.py                 # Configuración del panel de administración
│   ├── migrations/              # Migraciones de base de datos
│   └── templates/gestion/       # Templates HTML
│       ├── base.html            # Template base
│       ├── inicio.html          # Página de inicio
│       ├── cliente_*.html       # Templates de Cliente
│       ├── cuenta_*.html        # Templates de Cuenta
│       ├── transaccion_*.html   # Templates de Transacción
│       └── consultas.html       # Consultas personalizadas
└── requirements.txt             # Dependencias del proyecto
```

## Modelos de Datos

### 1. Cliente
Representa a los usuarios de la plataforma.

**Campos:**
- `nombre` (CharField): Nombre completo del cliente
- `email` (EmailField): Correo electrónico único
- `telefono` (CharField): Teléfono de contacto (opcional)
- `fecha_registro` (DateTimeField): Fecha de registro automática
- `activo` (BooleanField): Estado del cliente

**Relaciones:**
- Un cliente puede tener múltiples cuentas (One-to-Many con Cuenta)

### 2. TipoCuenta
Categorización de tipos de cuentas disponibles.

**Campos:**
- `nombre` (CharField): Nombre del tipo de cuenta (Ahorros, Corriente, etc.)
- `descripcion` (TextField): Descripción del tipo

### 3. Cuenta
Representa cuentas bancarias asociadas a clientes.

**Campos:**
- `cliente` (ForeignKey → Cliente): Propietario de la cuenta
- `tipo_cuenta` (ForeignKey → TipoCuenta): Tipo de cuenta
- `numero_cuenta` (CharField): Número único de cuenta
- `saldo` (DecimalField): Saldo actual
- `fecha_apertura` (DateTimeField): Fecha de apertura automática
- `fecha_cierre` (DateTimeField): Fecha de cierre (opcional)
- `activa` (BooleanField): Estado de la cuenta

**Relaciones:**
- Belongs To: Cliente (Many-to-One)
- Belongs To: TipoCuenta (Many-to-One)
- Has Many: Transacciones (One-to-Many)

### 4. Transaccion
Registra todas las transacciones realizadas en el sistema.

**Campos:**
- `cuenta_origen` (ForeignKey → Cuenta): Cuenta de origen
- `cuenta_destino` (ForeignKey → Cuenta): Cuenta de destino (opcional)
- `tipo` (CharField): Tipo de transacción (Depósito, Retiro, Transferencia, Pago)
- `monto` (DecimalField): Monto de la transacción
- `estado` (CharField): Estado (Pendiente, Completada, Fallida, Cancelada)
- `descripcion` (TextField): Descripción de la transacción
- `fecha_transaccion` (DateTimeField): Fecha automática
- `fecha_procesamiento` (DateTimeField): Fecha de procesamiento

**Relaciones:**
- Belongs To: Cuenta origen (Many-to-One)
- Belongs To: Cuenta destino (Many-to-One, opcional)

### 5. Reporte
Resúmenes y análisis de transacciones.

**Campos:**
- `cuenta` (OneToOneField → Cuenta): Cuenta asociada
- `total_transacciones` (IntegerField): Total de transacciones
- `monto_total_enviado` (DecimalField): Monto total enviado
- `monto_total_recibido` (DecimalField): Monto total recibido
- `fecha_generacion` (DateTimeField): Fecha de última actualización

**Relaciones:**
- Belongs To: Cuenta (One-to-One)

## Instrucciones de Instalación y Configuración

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Git (para control de versiones)

### Pasos de Instalación

1. **Clonar o descargar el repositorio**
   ```bash
   cd "d:\Clases Python\Proyecto Modulo 7"
   ```

2. **Crear entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activar entorno virtual**
   - **Windows:**
     ```bash
     .\venv\Scripts\activate
     ```
   - **Linux/Mac:**
     ```bash
     source venv/bin/activate
     ```

4. **Instalar dependencias**
   ```bash
   pip install django==6.0.4
   ```

   O usando requirements.txt (si existe):
   ```bash
   pip install -r requirements.txt
   ```

5. **Ejecutar migraciones**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Crear superusuario**
   ```bash
   python manage.py createsuperuser
   ```

   **Superusuario de demostración:**
   - Usuario: `admin`
   - Email: `admin@wallet.com`
   - Contraseña: (se solicitará en la terminal)

7. **Ejecutar servidor de desarrollo**
   ```bash
   python manage.py runserver
   ```

8. **Acceder a la aplicación**
   - URL Principal: http://127.0.0.1:8000/
   - Panel de Administración: http://127.0.0.1:8000/admin/

## Funcionalidades Principales

### 1. Operaciones CRUD Completas

#### Clientes
- **Listar:** Visualizar todos los clientes con paginación
- **Crear:** Registrar nuevos clientes
- **Ver:** Mostrar detalles y cuentas asociadas
- **Actualizar:** Editar información del cliente
- **Eliminar:** Cancelar clientes

#### Cuentas
- **Listar:** Ver todas las cuentas activas
- **Crear:** Abrir nuevas cuentas para clientes
- **Ver:** Detalles de cuenta y últimas transacciones
- **Actualizar:** Modificar información de la cuenta
- **Eliminar:** Cerrar cuentas

#### Transacciones
- **Listar:** Historial de todas las transacciones
- **Crear:** Registrar nuevas transacciones
- **Ver:** Detalles completos de cada transacción
- **Actualizar:** Modificar estado y descripción
- **Eliminar:** Cancelar transacciones

### 2. Consultas Personalizadas

El sistema implementa consultas avanzadas usando:

#### a) Cursor SQL Directo
```python
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT COUNT(*) as total FROM gestion_cliente WHERE activo = 1
    """)
    resultado = cursor.fetchone()
```

#### b) ORM con Annotate()
```python
saldo_promedio = Cuenta.objects.values('tipo_cuenta__nombre').annotate(
    promedio=Sum('saldo') / Count('id')
)
```

#### c) ORM con Filter() Avanzado
```python
clientes_multiples = Cliente.objects.annotate(
    total_cuentas=Count('cuentas')
).filter(total_cuentas__gt=1)
```

#### d) Método raw()
```python
clientes_con_telefono = Cliente.objects.raw(
    'SELECT * FROM gestion_cliente WHERE telefono IS NOT NULL'
)
```

### 3. Panel de Administración Django

Acceso a través de `/admin/`:
- Gestión completa de modelos
- Búsqueda y filtrado avanzado
- Interfaz intuitiva para CRUD
- Validaciones automáticas
- Auditoría de cambios

### 4. Seguridad

- **CSRF Protection:** Tokens CSRF en todos los formularios
- **Validaciones:** Validadores de campo a nivel de modelo
- **Permisos:** Sistema de autenticación de Django
- **Encriptación de Contraseña:** Almacenamiento seguro

## Rutas de la Aplicación

### Inicio y Generales
- `GET /` - Página de inicio (Dashboard)
- `GET /consultas/` - Consultas personalizadas

### Clientes
- `GET /clientes/` - Listar clientes
- `GET /clientes/<id>/` - Ver detalles de cliente
- `GET /clientes/crear/` - Formulario crear cliente
- `POST /clientes/crear/` - Guardar nuevo cliente
- `GET /clientes/<id>/actualizar/` - Formulario editar cliente
- `POST /clientes/<id>/actualizar/` - Guardar cambios cliente
- `GET /clientes/<id>/eliminar/` - Confirmar eliminación
- `POST /clientes/<id>/eliminar/` - Eliminar cliente

### Cuentas
- `GET /cuentas/` - Listar cuentas
- `GET /cuentas/<id>/` - Ver detalles de cuenta
- `GET /cuentas/crear/` - Formulario crear cuenta
- `POST /cuentas/crear/` - Guardar nueva cuenta
- `GET /cuentas/<id>/actualizar/` - Formulario editar cuenta
- `POST /cuentas/<id>/actualizar/` - Guardar cambios cuenta
- `GET /cuentas/<id>/eliminar/` - Confirmar eliminación
- `POST /cuentas/<id>/eliminar/` - Eliminar cuenta

### Transacciones
- `GET /transacciones/` - Listar transacciones
- `GET /transacciones/<id>/` - Ver detalles de transacción
- `GET /transacciones/crear/` - Formulario crear transacción
- `POST /transacciones/crear/` - Guardar nueva transacción
- `GET /transacciones/<id>/actualizar/` - Formulario editar transacción
- `POST /transacciones/<id>/actualizar/` - Guardar cambios transacción
- `GET /transacciones/<id>/eliminar/` - Confirmar eliminación
- `POST /transacciones/<id>/eliminar/` - Eliminar transacción

### Administración
- `GET /admin/` - Panel de administración

## Ejemplo de Uso desde Shell de Django

```bash
python manage.py shell
```

### Crear Cliente
```python
from gestion.models import Cliente

cliente = Cliente.objects.create(
    nombre="Juan García",
    email="juan@example.com",
    telefono="1234567890"
)
print(f"Cliente creado: {cliente}")
```

### Listar Clientes
```python
clientes = Cliente.objects.all()
for cliente in clientes:
    print(f"{cliente.nombre} - {cliente.email}")
```

### Filtrar Clientes
```python
clientes_activos = Cliente.objects.filter(activo=True)
clientes_por_nombre = Cliente.objects.filter(nombre__icontains='Juan')
```

### Actualizar Cliente
```python
cliente = Cliente.objects.get(email="juan@example.com")
cliente.telefono = "9876543210"
cliente.save()
```

### Eliminar Cliente
```python
cliente = Cliente.objects.get(email="juan@example.com")
cliente.delete()
```

### Consulta Personalizada
```python
from django.db import connection

with connection.cursor() as cursor:
    cursor.execute("SELECT * FROM gestion_cliente WHERE activo = 1")
    clientes = cursor.fetchall()
```

## Migraciones

### Crear Migraciones
Se ejecuta automáticamente cuando se modifican los modelos:
```bash
python manage.py makemigrations
```

### Aplicar Migraciones
```bash
python manage.py migrate
```

### Ver Estado de Migraciones
```bash
python manage.py showmigrations
```

### Ver SQL de Migraciones
```bash
python manage.py sqlmigrate gestion 0001
```

## Validaciones y Restricciones

1. **Email Único:** Cada cliente debe tener un email único
2. **Número de Cuenta Único:** Cada cuenta tiene un número único
3. **Saldo No Negativo:** El saldo no puede ser menor a 0
4. **Monto Transacción No Negativo:** El monto de transacción debe ser positivo
5. **Nombre Requerido:** Campo obligatorio para clientes
6. **Estado Válido:** Transacciones solo con estados permitidos

## Configuración para Producción

### Cambiar a PostgreSQL

En `websolutions_platform/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'alke_wallet_db',
        'USER': 'usuario_db',
        'PASSWORD': 'contraseña_segura',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### Instalar Adaptador PostgreSQL
```bash
pip install psycopg2-binary
```

### Configuraciones de Seguridad

```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com']
SECRET_KEY = 'tu-clave-secreta-segura'
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## Pruebas y Validación

### Ejecutar Pruebas
```bash
python manage.py test gestion
```

### Crear Datos de Prueba

Se puede usar el script de fixtures o crear datos manualmente desde el admin o shell:

```python
from gestion.models import Cliente, TipoCuenta, Cuenta, Transaccion

# Crear tipos de cuenta
tipo_ahorros = TipoCuenta.objects.create(
    nombre="Ahorros",
    descripcion="Cuenta de ahorros"
)

# Crear cliente
cliente = Cliente.objects.create(
    nombre="Ana García",
    email="ana@example.com",
    telefono="123456789"
)

# Crear cuenta
cuenta = Cuenta.objects.create(
    cliente=cliente,
    tipo_cuenta=tipo_ahorros,
    numero_cuenta="1001001001",
    saldo=1000.00
)

# Crear transacción
transaccion = Transaccion.objects.create(
    cuenta_origen=cuenta,
    tipo='DEPOSITO',
    monto=500.00,
    estado='COMPLETADA',
    descripcion='Depósito inicial'
)
```

## Mejoras Futuras

1. **Autenticación de Usuarios:** Implementar login/logout para clientes
2. **Dashboard Personal:** Cada usuario vea solo sus cuentas
3. **Notificaciones:** Alertas de transacciones importantes
4. **API REST:** Crear API para consumo desde aplicaciones móviles
5. **Reportes PDF:** Generar reportes descargables
6. **Gráficos:** Visualizar estadísticas con gráficos interactivos
7. **Autenticación Multi-factor:** Añadir seguridad adicional
8. **Auditoría Completa:** Registrar todas las acciones
9. **Internacionalización:** Soporte para múltiples idiomas
10. **Tests Unitarios:** Cobertura de pruebas al 100%

## Troubleshooting

### Error: "No such table"
**Solución:** Ejecutar migraciones
```bash
python manage.py migrate
```

### Error: "ModuleNotFoundError: No module named 'django'"
**Solución:** Instalar Django
```bash
pip install django==6.0.4
```

### Error: "Superuser creation failed"
**Solución:** Ejecutar migraciones antes de crear superusuario
```bash
python manage.py migrate
python manage.py createsuperuser
```

### Puerto 8000 ya está en uso
**Solución:** Usar otro puerto
```bash
python manage.py runserver 8001
```

## Conclusión

Alke Wallet demuestra la implementación completa de una aplicación Django con:
- Modelos bien estructurados con relaciones complejas
- Operaciones CRUD funcionales
- Consultas personalizadas avanzadas
- Seguridad incorporada
- Interfaz de usuario responsiva
- Escalabilidad para producción

El proyecto está listo para ser extendido con características adicionales según los requerimientos del negocio.

## Contacto y Soporte

Para preguntas o soporte técnico, contactar al equipo de desarrollo de Alke Financial.

---

**Última actualización:** Abril 2026
**Versión:** 1.0.0
**Licencia:** Todos los derechos reservados © Alke Financial
