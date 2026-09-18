from django.urls import path
from . import views

urlpatterns = [
    path("nuevo/", views.nuevo_pedido, name="nuevo_pedido"),
    path("agenda/", views.agenda, name="agenda"),
    path("pedido/<int:pedido_id>/avanzar/", views.avanzar_estado, name="avanzar_estado"),
    path("backup/", views.backup_db_view, name="backup_db_view"),
]