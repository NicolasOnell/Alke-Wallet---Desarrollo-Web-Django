from django.contrib import admin
from .models import Cliente, TipoCuenta, Cuenta, Transaccion, Reporte


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    """
    Administración de Clientes con opciones de filtrado y búsqueda.
    """
    list_display = ('nombre', 'email', 'telefono', 'fecha_registro', 'activo')
    list_filter = ('activo', 'fecha_registro')
    search_fields = ('nombre', 'email', 'telefono')
    readonly_fields = ('fecha_registro',)
    fieldsets = (
        ('Información Personal', {
            'fields': ('nombre', 'email', 'telefono')
        }),
        ('Estado', {
            'fields': ('activo', 'fecha_registro')
        }),
    )


@admin.register(TipoCuenta)
class TipoCuentaAdmin(admin.ModelAdmin):
    """
    Administración de Tipos de Cuenta.
    """
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    """
    Administración de Cuentas con relación a Clientes.
    """
    list_display = ('numero_cuenta', 'cliente', 'tipo_cuenta', 'saldo', 
                    'fecha_apertura', 'activa')
    list_filter = ('activa', 'fecha_apertura', 'tipo_cuenta')
    search_fields = ('numero_cuenta', 'cliente__nombre', 'cliente__email')
    readonly_fields = ('fecha_apertura',)
    fieldsets = (
        ('Información de Cuenta', {
            'fields': ('cliente', 'tipo_cuenta', 'numero_cuenta', 'saldo')
        }),
        ('Fecha', {
            'fields': ('fecha_apertura', 'fecha_cierre')
        }),
        ('Estado', {
            'fields': ('activa',)
        }),
    )


@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    """
    Administración de Transacciones con filtros por tipo y estado.
    """
    list_display = ('id', 'tipo', 'monto', 'estado', 'cuenta_origen', 
                    'cuenta_destino', 'fecha_transaccion')
    list_filter = ('tipo', 'estado', 'fecha_transaccion')
    search_fields = ('cuenta_origen__numero_cuenta', 
                     'cuenta_destino__numero_cuenta', 'descripcion')
    readonly_fields = ('fecha_transaccion',)
    fieldsets = (
        ('Información de Transacción', {
            'fields': ('tipo', 'monto', 'estado')
        }),
        ('Cuentas', {
            'fields': ('cuenta_origen', 'cuenta_destino')
        }),
        ('Descripción', {
            'fields': ('descripcion',)
        }),
        ('Fechas', {
            'fields': ('fecha_transaccion', 'fecha_procesamiento')
        }),
    )


@admin.register(Reporte)
class ReporteAdmin(admin.ModelAdmin):
    """
    Administración de Reportes de Transacciones.
    """
    list_display = ('cuenta', 'total_transacciones', 'monto_total_enviado', 
                    'monto_total_recibido', 'fecha_generacion')
    list_filter = ('fecha_generacion',)
    search_fields = ('cuenta__numero_cuenta',)
    readonly_fields = ('total_transacciones', 'monto_total_enviado', 
                      'monto_total_recibido', 'fecha_generacion')
