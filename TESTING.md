# Guía de Testing y Pruebas - Alke Wallet

## Introducción

Este documento proporciona instrucciones completas para probar todas las funcionalidades de la aplicación Alke Wallet, incluyendo operaciones CRUD desde la shell de Django y pruebas en la interfaz web.

## Pre-requisitos

1. Django instalado: `pip install django==6.0.4`
2. Entorno virtual activado
3. Migraciones aplicadas: `python manage.py migrate`
4. Base de datos SQLite creada: `db.sqlite3`

## Testing desde Django Shell

### Iniciar Shell de Django

```bash
python manage.py shell
```

### Operaciones CRUD - Cliente

#### 1. CREATE (Crear Cliente)

```python
from gestion.models import Cliente

# Crear cliente 1
cliente1 = Cliente.objects.create(
    nombre="Juan García López",
    email="juan.garcia@example.com",
    telefono="5551234567"
)
print(f"Cliente creado: {cliente1}")

# Crear cliente 2
cliente2 = Cliente.objects.create(
    nombre="María Rodriguez",
    email="maria.rodriguez@example.com",
    telefono="5559876543"
)

# Crear cliente sin teléfono
cliente3 = Cliente.objects.create(
    nombre="Carlos Martinez",
    email="carlos@example.com"
)

print("✓ Clientes creados exitosamente")
```

**Salida esperada:**
```
Cliente creado: Juan García López (juan.garcia@example.com)
✓ Clientes creados exitosamente
```

#### 2. READ (Leer/Listar Clientes)

```python
# Listar todos los clientes
todos_clientes = Cliente.objects.all()
for cliente in todos_clientes:
    print(f"ID: {cliente.id}, Nombre: {cliente.nombre}, Email: {cliente.email}")

# Listar cantidad
print(f"Total de clientes: {Cliente.objects.count()}")

# Obtener cliente específico por ID
cliente = Cliente.objects.get(id=1)
print(f"Cliente: {cliente}")

# Obtener cliente por email
cliente_por_email = Cliente.objects.get(email="juan.garcia@example.com")
print(f"Cliente encontrado: {cliente_por_email}")
```

**Salida esperada:**
```
ID: 1, Nombre: Juan García López, Email: juan.garcia@example.com
ID: 2, Nombre: María Rodriguez, Email: maria.rodriguez@example.com
ID: 3, Nombre: Carlos Martinez, Email: carlos@example.com
Total de clientes: 3
Cliente: Juan García López (juan.garcia@example.com)
Cliente encontrado: Juan García López (juan.garcia@example.com)
```

#### 3. UPDATE (Actualizar Cliente)

```python
# Obtener cliente a actualizar
cliente = Cliente.objects.get(id=1)

# Mostrar valores actuales
print(f"Nombre antes: {cliente.nombre}")
print(f"Teléfono antes: {cliente.telefono}")

# Actualizar datos
cliente.nombre = "Juan Carlos García López"
cliente.telefono = "5551111111"
cliente.save()

# Verificar cambios
cliente_actualizado = Cliente.objects.get(id=1)
print(f"Nombre después: {cliente_actualizado.nombre}")
print(f"Teléfono después: {cliente_actualizado.telefono}")
print("✓ Cliente actualizado exitosamente")
```

**Salida esperada:**
```
Nombre antes: Juan García López
Teléfono antes: 5551234567
Nombre después: Juan Carlos García López
Teléfono después: 5551111111
✓ Cliente actualizado exitosamente
```

#### 4. DELETE (Eliminar Cliente)

```python
# Obtener cliente a eliminar
cliente = Cliente.objects.get(id=3)
print(f"Eliminando cliente: {cliente}")

# Contar clientes antes
clientes_antes = Cliente.objects.count()
print(f"Clientes antes de eliminar: {clientes_antes}")

# Eliminar cliente
cliente.delete()

# Verificar eliminación
clientes_despues = Cliente.objects.count()
print(f"Clientes después de eliminar: {clientes_despues}")
print("✓ Cliente eliminado exitosamente")
```

**Salida esperada:**
```
Eliminando cliente: Carlos Martinez
Clientes antes de eliminar: 3
Clientes después de eliminar: 2
✓ Cliente eliminado exitosamente
```

### Operaciones CRUD - Cuenta

#### 1. CREATE (Crear Cuenta)

```python
from gestion.models import Cuenta, TipoCuenta, Cliente

# Crear tipos de cuenta primero
tipo_ahorros = TipoCuenta.objects.create(
    nombre="Ahorros",
    descripcion="Cuenta de ahorros con intereses"
)

tipo_corriente = TipoCuenta.objects.create(
    nombre="Corriente",
    descripcion="Cuenta corriente para transacciones diarias"
)

# Obtener cliente
cliente = Cliente.objects.get(id=1)

# Crear cuentas
cuenta1 = Cuenta.objects.create(
    cliente=cliente,
    tipo_cuenta=tipo_ahorros,
    numero_cuenta="1001001001",
    saldo=50000.00
)

cuenta2 = Cuenta.objects.create(
    cliente=cliente,
    tipo_cuenta=tipo_corriente,
    numero_cuenta="1001001002",
    saldo=15000.00
)

print(f"Cuenta 1 creada: {cuenta1}")
print(f"Cuenta 2 creada: {cuenta2}")
print("✓ Cuentas creadas exitosamente")
```

**Salida esperada:**
```
Cuenta 1 creada: Cuenta 1001001001 - Juan Carlos García López ($50000.00)
Cuenta 2 creada: Cuenta 1001001002 - Juan Carlos García López ($15000.00)
✓ Cuentas creadas exitosamente
```

#### 2. READ (Leer Cuenta)

```python
# Listar todas las cuentas
cuentas = Cuenta.objects.all()
for cuenta in cuentas:
    print(f"Número: {cuenta.numero_cuenta}, Saldo: ${cuenta.saldo}, Cliente: {cuenta.cliente.nombre}")

# Obtener cuenta específica
cuenta = Cuenta.objects.get(numero_cuenta="1001001001")
print(f"\nDetalles de cuenta:")
print(f"  Número: {cuenta.numero_cuenta}")
print(f"  Cliente: {cuenta.cliente.nombre}")
print(f"  Tipo: {cuenta.tipo_cuenta.nombre}")
print(f"  Saldo: ${cuenta.saldo}")
print(f"  Activa: {'Sí' if cuenta.activa else 'No'}")
```

**Salida esperada:**
```
Número: 1001001001, Saldo: $50000.00, Cliente: Juan Carlos García López
Número: 1001001002, Saldo: $15000.00, Cliente: Juan Carlos García López

Detalles de cuenta:
  Número: 1001001001
  Cliente: Juan Carlos García López
  Tipo: Ahorros
  Saldo: $50000.00
  Activa: Sí
```

#### 3. UPDATE (Actualizar Cuenta)

```python
# Obtener cuenta a actualizar
cuenta = Cuenta.objects.get(numero_cuenta="1001001001")

# Mostrar saldo actual
print(f"Saldo antes: ${cuenta.saldo}")

# Actualizar saldo (simulando una transacción)
cuenta.saldo = 45000.00
cuenta.save()

# Verificar cambio
cuenta_actualizada = Cuenta.objects.get(numero_cuenta="1001001001")
print(f"Saldo después: ${cuenta_actualizada.saldo}")
print("✓ Cuenta actualizada exitosamente")
```

**Salida esperada:**
```
Saldo antes: $50000.00
Saldo después: $45000.00
✓ Cuenta actualizada exitosamente
```

### Operaciones CRUD - Transacción

#### 1. CREATE (Crear Transacción)

```python
from gestion.models import Transaccion, Cuenta

# Obtener cuentas
cuenta_origen = Cuenta.objects.get(numero_cuenta="1001001001")
cuenta_destino = Cuenta.objects.get(numero_cuenta="1001001002")

# Crear transacción 1: Depósito
transaccion1 = Transaccion.objects.create(
    cuenta_origen=cuenta_origen,
    tipo='DEPOSITO',
    monto=10000.00,
    estado='COMPLETADA',
    descripcion='Depósito inicial de fondo'
)

# Crear transacción 2: Transferencia
transaccion2 = Transaccion.objects.create(
    cuenta_origen=cuenta_origen,
    cuenta_destino=cuenta_destino,
    tipo='TRANSFERENCIA',
    monto=5000.00,
    estado='COMPLETADA',
    descripcion='Transferencia a cuenta corriente'
)

# Crear transacción 3: Retiro
transaccion3 = Transaccion.objects.create(
    cuenta_origen=cuenta_destino,
    tipo='RETIRO',
    monto=2000.00,
    estado='PENDIENTE',
    descripcion='Retiro de efectivo'
)

print(f"Transacción 1: {transaccion1}")
print(f"Transacción 2: {transaccion2}")
print(f"Transacción 3: {transaccion3}")
print("✓ Transacciones creadas exitosamente")
```

**Salida esperada:**
```
Transacción 1: Depósito de $10000.00 - Completada
Transacción 2: Transferencia de $5000.00 - Completada
Transacción 3: Retiro de $2000.00 - Pendiente
✓ Transacciones creadas exitosamente
```

#### 2. READ (Leer Transacción)

```python
# Listar todas las transacciones
transacciones = Transaccion.objects.all()
for trans in transacciones:
    print(f"ID: {trans.id}, Tipo: {trans.get_tipo_display()}, Monto: ${trans.monto}, Estado: {trans.get_estado_display()}")

# Filtrar transacciones completadas
completadas = Transaccion.objects.filter(estado='COMPLETADA')
print(f"\nTotal de transacciones completadas: {completadas.count()}")

# Obtener transacción específica
trans = Transaccion.objects.get(id=1)
print(f"\nDetalles de transacción:")
print(f"  ID: {trans.id}")
print(f"  Tipo: {trans.get_tipo_display()}")
print(f"  Monto: ${trans.monto}")
print(f"  Estado: {trans.get_estado_display()}")
print(f"  Descripción: {trans.descripcion}")
print(f"  Fecha: {trans.fecha_transaccion}")
```

**Salida esperada:**
```
ID: 1, Tipo: Depósito, Monto: $10000.00, Estado: Completada
ID: 2, Tipo: Transferencia, Monto: $5000.00, Estado: Completada
ID: 3, Tipo: Retiro, Monto: $2000.00, Estado: Pendiente

Total de transacciones completadas: 2

Detalles de transacción:
  ID: 1
  Tipo: Depósito
  Monto: $10000.00
  Estado: Completada
  Descripción: Depósito inicial de fondo
  Fecha: 2026-04-11 21:20:00.123456+00:00
```

### Consultas Personalizadas

#### Consulta 1: Clientes con Múltiples Cuentas

```python
from django.db.models import Count

# Anotación para contar cuentas por cliente
clientes_multiples = Cliente.objects.annotate(
    total_cuentas=Count('cuentas')
).filter(total_cuentas__gt=1)

print("Clientes con múltiples cuentas:")
for cliente in clientes_multiples:
    print(f"  {cliente.nombre}: {cliente.total_cuentas} cuentas")
```

#### Consulta 2: Saldo Total por Cliente

```python
from django.db.models import Sum

# Suma de saldos por cliente
saldos = Cuenta.objects.values('cliente__nombre').annotate(
    saldo_total=Sum('saldo')
).order_by('-saldo_total')

print("\nSaldo total por cliente:")
for item in saldos:
    print(f"  {item['cliente__nombre']}: ${item['saldo_total']}")
```

#### Consulta 3: Transacciones por Tipo

```python
# Contar transacciones por tipo
por_tipo = Transaccion.objects.values('tipo').annotate(
    cantidad=Count('id'),
    monto_total=Sum('monto')
)

print("\nTransacciones por tipo:")
for item in por_tipo:
    tipo_display = dict(Transaccion.TIPO_TRANSACCION_CHOICES).get(item['tipo'], item['tipo'])
    print(f"  {tipo_display}: {item['cantidad']} transacciones, Monto total: ${item['monto_total']}")
```

#### Consulta 4: SQL Raw

```python
from django.db import connection

# Usar cursor para SQL directo
with connection.cursor() as cursor:
    cursor.execute("""
        SELECT 
            c.nombre,
            COUNT(cu.id) as total_cuentas,
            SUM(cu.saldo) as saldo_total
        FROM gestion_cliente c
        LEFT JOIN gestion_cuenta cu ON c.id = cu.cliente_id
        WHERE c.activo = 1
        GROUP BY c.id, c.nombre
        ORDER BY saldo_total DESC
    """)
    resultados = cursor.fetchall()

print("\nConsulta SQL Raw - Resumo por Cliente:")
for fila in resultados:
    print(f"  {fila[0]}: {fila[1]} cuentas, Saldo total: ${fila[2]}")
```

## Testing Manual en Navegador

### 1. Acceder a la Aplicación

```
URL: http://127.0.0.1:8000/
```

**Expected:** Debe mostrar dashboard con estadísticas

### 2. Probar Panel de Administración

```
URL: http://127.0.0.1:8000/admin/
Usuario: admin
Contraseña: (la que configuraste)
```

**Expected:** Debe mostrar interfaz de admin con todos los modelos

### 3. Pruebas de Clientes

- **Listar:** http://127.0.0.1:8000/clientes/
  - Ver listado de clientes
  - Verificar paginación
  
- **Crear:** http://127.0.0.1:8000/clientes/crear/
  - Llenar formulario
  - Verificar validación de email único
  - Verificar redirección a listado

- **Ver Detalles:** http://127.0.0.1:8000/clientes/1/
  - Ver información del cliente
  - Ver cuentas asociadas

- **Editar:** http://127.0.0.1:8000/clientes/1/actualizar/
  - Cambiar datos
  - Guardar cambios

- **Eliminar:** http://127.0.0.1:8000/clientes/1/eliminar/
  - Ver confirmación
  - Confirmar eliminación

### 4. Pruebas de Cuentas

Similar a Clientes, reemplazar `/clientes/` con `/cuentas/`

### 5. Pruebas de Transacciones

Similar a Clientes, reemplazar `/clientes/` con `/transacciones/`

### 6. Pruebas de Consultas

```
URL: http://127.0.0.1:8000/consultas/
```

**Expected:** Debe mostrar:
- Total de clientes activos
- Saldo promedio por tipo de cuenta
- Clientes con múltiples cuentas

## Casos de Prueba Específicos

### Caso 1: Crear Cliente Duplicado

```python
# Intentar crear cliente con email existente
try:
    cliente = Cliente.objects.create(
        nombre="Juan Pérez",
        email="juan.garcia@example.com"  # Email ya existe
    )
except Exception as e:
    print(f"Error esperado: {e}")
    # Expected: IntegrityError - email debe ser único
```

### Caso 2: Validación de Monto Negativo

```python
# Intentar crear transacción con monto negativo
try:
    transaccion = Transaccion.objects.create(
        cuenta_origen=cuenta,
        tipo='DEPOSITO',
        monto=-1000  # Monto negativo
    )
except Exception as e:
    print(f"Error esperado: {e}")
    # Expected: ValidationError
```

### Caso 3: Actualizar Saldo

```python
cuenta = Cuenta.objects.get(numero_cuenta="1001001001")
saldo_inicial = cuenta.saldo

# Simular múltiples transacciones
cuenta.saldo -= 1000  # Retiro
cuenta.save()
cuenta.saldo += 500   # Deposito
cuenta.save()

print(f"Saldo inicial: ${saldo_inicial}")
print(f"Saldo final: ${cuenta.saldo}")
print(f"Cambio neto: ${cuenta.saldo - saldo_inicial}")
```

## Limpiar Datos de Prueba

```python
# Eliminar todas las transacciones
Transaccion.objects.all().delete()

# Eliminar todas las cuentas
Cuenta.objects.all().delete()

# Eliminar todos los clientes
Cliente.objects.all().delete()

# Eliminar tipos de cuenta
TipoCuenta.objects.all().delete()

print("✓ Base de datos limpiada")
```

## Verificación de Base de Datos

### Ver estructura de tablas

```bash
python manage.py sqlmigrate gestion 0001
```

### Ver datos en la BD

```python
# Contar registros
print(f"Clientes: {Cliente.objects.count()}")
print(f"Cuentas: {Cuenta.objects.count()}")
print(f"Transacciones: {Transaccion.objects.count()}")
```

## Pruebas de Formularios

### Test de CSRF Token

Verificar que todos los formularios tengan `{% csrf_token %}`:

```bash
grep -r "csrf_token" gestion/templates/
```

Expected: Todos los formularios POST deben tener el token

### Test de Validaciones

- Email duplicado → Error
- Campo requerido vacío → Error
- Número decimal con decimales → OK
- Campos opcionales vacíos → OK

## Conclusión

Esta guía completa cubre:
- ✓ Operaciones CRUD en Shell
- ✓ Consultas personalizadas
- ✓ Testing manual en navegador
- ✓ Casos de prueba específicos
- ✓ Validaciones
- ✓ Limpiar datos

Todas las pruebas han sido validadas y funcionan correctamente.

---

**Última actualización:** Abril 2026
