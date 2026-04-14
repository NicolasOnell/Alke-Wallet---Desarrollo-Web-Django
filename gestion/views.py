from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q, Sum, Count
from django.db import connection
from .models import Cliente, Cuenta, Transaccion, TipoCuenta, Reporte


# ===================== VISTAS DE CLIENTE =====================

class ClienteListView(LoginRequiredMixin, ListView):
    """
    Vista para listar todos los clientes.
    """
    model = Cliente
    template_name = 'gestion/cliente_list.html'
    context_object_name = 'clientes'
    paginate_by = 10


class ClienteDetailView(DetailView):
    """
    Vista para ver detalles de un cliente específico.
    """
    model = Cliente
    template_name = 'gestion/cliente_detail.html'
    context_object_name = 'cliente'


class ClienteCreateView(CreateView):
    """
    Vista para crear un nuevo cliente.
    """
    model = Cliente
    template_name = 'gestion/cliente_form.html'
    fields = ['nombre', 'email', 'telefono', 'activo']
    success_url = reverse_lazy('cliente-list')


class ClienteUpdateView(UpdateView):
    """
    Vista para actualizar un cliente existente.
    """
    model = Cliente
    template_name = 'gestion/cliente_form.html'
    fields = ['nombre', 'email', 'telefono', 'activo']
    success_url = reverse_lazy('cliente-list')


class ClienteDeleteView(DeleteView):
    """
    Vista para eliminar un cliente.
    """
    model = Cliente
    template_name = 'gestion/cliente_confirm_delete.html'
    success_url = reverse_lazy('cliente-list')


# ===================== VISTAS DE CUENTA =====================

class CuentaListView(ListView):
    """
    Vista para listar todas las cuentas.
    """
    model = Cuenta
    template_name = 'gestion/cuenta_list.html'
    context_object_name = 'cuentas'
    paginate_by = 10


class CuentaDetailView(DetailView):
    """
    Vista para ver detalles de una cuenta específica.
    """
    model = Cuenta
    template_name = 'gestion/cuenta_detail.html'
    context_object_name = 'cuenta'


class CuentaCreateView(CreateView):
    """
    Vista para crear una nueva cuenta.
    """
    model = Cuenta
    template_name = 'gestion/cuenta_form.html'
    fields = ['cliente', 'tipo_cuenta', 'numero_cuenta', 'saldo', 'activa']
    success_url = reverse_lazy('cuenta-list')


class CuentaUpdateView(UpdateView):
    """
    Vista para actualizar una cuenta existente.
    """
    model = Cuenta
    template_name = 'gestion/cuenta_form.html'
    fields = ['cliente', 'tipo_cuenta', 'numero_cuenta', 'saldo', 'activa']
    success_url = reverse_lazy('cuenta-list')


class CuentaDeleteView(DeleteView):
    """
    Vista para eliminar una cuenta.
    """
    model = Cuenta
    template_name = 'gestion/cuenta_confirm_delete.html'
    success_url = reverse_lazy('cuenta-list')


# ===================== VISTAS DE TRANSACCION =====================

class TransaccionListView(ListView):
    """
    Vista para listar todas las transacciones.
    """
    model = Transaccion
    template_name = 'gestion/transaccion_list.html'
    context_object_name = 'transacciones'
    paginate_by = 10


class TransaccionDetailView(DetailView):
    """
    Vista para ver detalles de una transacción específica.
    """
    model = Transaccion
    template_name = 'gestion/transaccion_detail.html'
    context_object_name = 'transaccion'


class TransaccionCreateView(CreateView):
    """
    Vista para crear una nueva transacción.
    """
    model = Transaccion
    template_name = 'gestion/transaccion_form.html'
    fields = ['cuenta_origen', 'cuenta_destino', 'tipo', 'monto', 
              'estado', 'descripcion']
    success_url = reverse_lazy('transaccion-list')


class TransaccionUpdateView(UpdateView):
    """
    Vista para actualizar una transacción existente.
    """
    model = Transaccion
    template_name = 'gestion/transaccion_form.html'
    fields = ['cuenta_origen', 'cuenta_destino', 'tipo', 'monto', 
              'estado', 'descripcion']
    success_url = reverse_lazy('transaccion-list')


class TransaccionDeleteView(DeleteView):
    """
    Vista para eliminar una transacción.
    """
    model = Transaccion
    template_name = 'gestion/transaccion_confirm_delete.html'
    success_url = reverse_lazy('transaccion-list')


# ===================== VISTAS DE INICIO Y CONSULTAS PERSONALIZADAS =====================

def inicio(request):
    """
    Vista de inicio con estadísticas generales.
    """
    total_clientes = Cliente.objects.filter(activo=True).count()
    total_cuentas = Cuenta.objects.filter(activa=True).count()
    total_transacciones = Transaccion.objects.count()
    
    # Consulta personalizada con raw()
    clientes_con_telefono = Cliente.objects.raw(
        'SELECT * FROM gestion_cliente WHERE telefono IS NOT NULL'
    )
    cantidad_con_telefono = sum(1 for _ in clientes_con_telefono)
    
    # Estadísticas de transacciones
    stats_transacciones = Transaccion.objects.values('tipo').annotate(
        total=Count('id'),
        monto_total=Sum('monto')
    )
    
    context = {
        'total_clientes': total_clientes,
        'total_cuentas': total_cuentas,
        'total_transacciones': total_transacciones,
        'cantidad_con_telefono': cantidad_con_telefono,
        'stats_transacciones': stats_transacciones,
    }
    
    return render(request, 'gestion/inicio.html', context)


def consultas_personalizadas(request):
    """
    Vista que demuestra consultas personalizadas con SQL.
    """
    # Consulta 1: Total de clientes por estado
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT COUNT(*) as total FROM gestion_cliente WHERE activo = 1
        """)
        total_activos = cursor.fetchone()[0]
    
    # Consulta 2: Saldo promedio por tipo de cuenta
    saldo_promedio = Cuenta.objects.values('tipo_cuenta__nombre').annotate(
        promedio=Sum('saldo') / Count('id')
    )
    
    # Consulta 3: Clientes con más de una cuenta
    clientes_multiples = Cliente.objects.annotate(
        total_cuentas=Count('cuentas')
    ).filter(total_cuentas__gt=1)
    
    context = {
        'total_activos': total_activos,
        'saldo_promedio': saldo_promedio,
        'clientes_multiples': clientes_multiples,
    }
    
    return render(request, 'gestion/consultas.html', context)
