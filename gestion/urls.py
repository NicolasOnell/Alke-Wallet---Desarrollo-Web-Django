from django.urls import path
from . import views

app_name = 'gestion'

urlpatterns = [
    # URL de inicio
    path('', views.inicio, name='inicio'),
    path('consultas/', views.consultas_personalizadas, name='consultas'),
    
    # URLs de Cliente
    path('clientes/', views.ClienteListView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', views.ClienteDetailView.as_view(), name='cliente-detail'),
    path('clientes/crear/', views.ClienteCreateView.as_view(), name='cliente-create'),
    path('clientes/<int:pk>/actualizar/', views.ClienteUpdateView.as_view(), name='cliente-update'),
    path('clientes/<int:pk>/eliminar/', views.ClienteDeleteView.as_view(), name='cliente-delete'),
    
    # URLs de Cuenta
    path('cuentas/', views.CuentaListView.as_view(), name='cuenta-list'),
    path('cuentas/<int:pk>/', views.CuentaDetailView.as_view(), name='cuenta-detail'),
    path('cuentas/crear/', views.CuentaCreateView.as_view(), name='cuenta-create'),
    path('cuentas/<int:pk>/actualizar/', views.CuentaUpdateView.as_view(), name='cuenta-update'),
    path('cuentas/<int:pk>/eliminar/', views.CuentaDeleteView.as_view(), name='cuenta-delete'),
    
    # URLs de Transacción
    path('transacciones/', views.TransaccionListView.as_view(), name='transaccion-list'),
    path('transacciones/<int:pk>/', views.TransaccionDetailView.as_view(), name='transaccion-detail'),
    path('transacciones/crear/', views.TransaccionCreateView.as_view(), name='transaccion-create'),
    path('transacciones/<int:pk>/actualizar/', views.TransaccionUpdateView.as_view(), name='transaccion-update'),
    path('transacciones/<int:pk>/eliminar/', views.TransaccionDeleteView.as_view(), name='transaccion-delete'),
]
