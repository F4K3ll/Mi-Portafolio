from django.contrib import admin
from .models import Cliente, Producto, Pedido


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("nombre", "telefono")
    search_fields = ("nombre",)


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("sabor", "tipo")
    list_filter = ("tipo",)


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ("cliente", "producto", "cantidad", "fecha_entrega", "estado")
    list_filter = ("estado", "fecha_entrega")
    search_fields = ("cliente__nombre",)