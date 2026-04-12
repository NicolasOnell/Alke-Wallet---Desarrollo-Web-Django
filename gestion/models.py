from django.db import models
from django.core.validators import MinValueValidator
from django.utils import timezone


class Cliente(models.Model):
    """
    Modelo de Cliente para la billetera digital Alke Wallet.
    Representa a los usuarios de la plataforma.
    """
    nombre = models.CharField(max_length=100, help_text="Nombre completo del cliente")
    email = models.EmailField(unique=True, help_text="Correo electrónico único")
    telefono = models.CharField(max_length=20, blank=True, null=True, 
                                help_text="Teléfono de contacto")
    fecha_registro = models.DateTimeField(auto_now_add=True, 
                                         help_text="Fecha de registro del cliente")
    activo = models.BooleanField(default=True, help_text="Estado del cliente")
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-fecha_registro']
        indexes = [
            models.Index(fields=['email']),
            models.Index(fields=['nombre']),
        ]
    
    def __str__(self):
        return f"{self.nombre} ({self.email})"


class TipoCuenta(models.Model):
    """
    Modelo para los tipos de cuenta disponibles (Ahorros, Corriente, etc.)
    """
    nombre = models.CharField(max_length=50, unique=True, 
                             help_text="Nombre del tipo de cuenta")
    descripcion = models.TextField(blank=True, null=True, 
                                   help_text="Descripción del tipo de cuenta")
    
    class Meta:
        verbose_name = "Tipo de Cuenta"
        verbose_name_plural = "Tipos de Cuenta"
    
    def __str__(self):
        return self.nombre


class Cuenta(models.Model):
    """
    Modelo de Cuenta asociado a un Cliente.
    Relación: Un Cliente puede tener múltiples Cuentas.
    """
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, 
                               related_name='cuentas',
                               help_text="Cliente propietario de la cuenta")
    tipo_cuenta = models.ForeignKey(TipoCuenta, on_delete=models.SET_NULL, 
                                    null=True, blank=True,
                                    help_text="Tipo de cuenta")
    numero_cuenta = models.CharField(max_length=20, unique=True, 
                                    help_text="Número único de cuenta")
    saldo = models.DecimalField(max_digits=12, decimal_places=2, 
                               default=0, validators=[MinValueValidator(0)],
                               help_text="Saldo actual de la cuenta")
    fecha_apertura = models.DateTimeField(auto_now_add=True, 
                                         help_text="Fecha de apertura")
    fecha_cierre = models.DateTimeField(null=True, blank=True, 
                                       help_text="Fecha de cierre (si aplica)")
    activa = models.BooleanField(default=True, help_text="Estado de la cuenta")
    
    class Meta:
        verbose_name = "Cuenta"
        verbose_name_plural = "Cuentas"
        ordering = ['-fecha_apertura']
        unique_together = ['cliente', 'numero_cuenta']
    
    def __str__(self):
        return f"Cuenta {self.numero_cuenta} - {self.cliente.nombre} (${self.saldo})"


class Transaccion(models.Model):
    """
    Modelo de Transacciones entre cuentas.
    Relación: Una Transacción está asociada a una Cuenta origen y puede tener una destino.
    """
    TIPO_TRANSACCION_CHOICES = [
        ('DEPOSITO', 'Depósito'),
        ('RETIRO', 'Retiro'),
        ('TRANSFERENCIA', 'Transferencia'),
        ('PAGO', 'Pago'),
    ]
    
    ESTADO_CHOICES = [
        ('PENDIENTE', 'Pendiente'),
        ('COMPLETADA', 'Completada'),
        ('FALLIDA', 'Fallida'),
        ('CANCELADA', 'Cancelada'),
    ]
    
    cuenta_origen = models.ForeignKey(Cuenta, on_delete=models.CASCADE, 
                                     related_name='transacciones_enviadas',
                                     help_text="Cuenta de origen")
    cuenta_destino = models.ForeignKey(Cuenta, on_delete=models.SET_NULL, 
                                      null=True, blank=True, 
                                      related_name='transacciones_recibidas',
                                      help_text="Cuenta de destino (si aplica)")
    tipo = models.CharField(max_length=20, choices=TIPO_TRANSACCION_CHOICES, 
                           help_text="Tipo de transacción")
    monto = models.DecimalField(max_digits=12, decimal_places=2, 
                               validators=[MinValueValidator(0)],
                               help_text="Monto de la transacción")
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, 
                             default='PENDIENTE',
                             help_text="Estado actual de la transacción")
    descripcion = models.TextField(blank=True, null=True, 
                                  help_text="Descripción de la transacción")
    fecha_transaccion = models.DateTimeField(auto_now_add=True, 
                                            help_text="Fecha y hora de la transacción")
    fecha_procesamiento = models.DateTimeField(null=True, blank=True, 
                                              help_text="Fecha de procesamiento")
    
    class Meta:
        verbose_name = "Transacción"
        verbose_name_plural = "Transacciones"
        ordering = ['-fecha_transaccion']
        indexes = [
            models.Index(fields=['cuenta_origen', 'fecha_transaccion']),
            models.Index(fields=['estado']),
            models.Index(fields=['tipo']),
        ]
    
    def __str__(self):
        if self.cuenta_destino:
            return f"{self.get_tipo_display()} de ${self.monto} - {self.get_estado_display()}"
        return f"{self.get_tipo_display()} de ${self.monto} - {self.get_estado_display()}"


class Reporte(models.Model):
    """
    Modelo para generar reportes de transacciones.
    Relación: Un Reporte está asociado a una Cuenta.
    """
    cuenta = models.OneToOneField(Cuenta, on_delete=models.CASCADE, 
                                 related_name='reporte',
                                 help_text="Cuenta asociada al reporte")
    total_transacciones = models.IntegerField(default=0, 
                                             help_text="Total de transacciones")
    monto_total_enviado = models.DecimalField(max_digits=12, decimal_places=2, 
                                             default=0,
                                             help_text="Monto total enviado")
    monto_total_recibido = models.DecimalField(max_digits=12, decimal_places=2, 
                                              default=0,
                                              help_text="Monto total recibido")
    fecha_generacion = models.DateTimeField(auto_now=True, 
                                           help_text="Fecha de última actualización del reporte")
    
    class Meta:
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"
    
    def __str__(self):
        return f"Reporte de {self.cuenta.numero_cuenta}"
