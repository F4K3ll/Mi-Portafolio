from django.urls import path
from . import views

urlpatterns = [
    path("nuevo/", views.nuevo_pedido, name="nuevo_pedido"),
]