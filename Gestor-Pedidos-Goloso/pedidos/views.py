from datetime import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone

from .forms import PedidoForm
from .models import Pedido

@staff_member_required
def nuevo_pedido(request):
    if request.method == "POST":
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Pedido guardado correctamente.")
            return redirect("nuevo_pedido")
    else:
        form = PedidoForm()
    return render(request, "pedidos/nuevo_pedido.html", {"form": form})


@staff_member_required
def agenda(request):
    fecha_str = request.GET.get("fecha")
    if fecha_str:
        try:
            fecha = datetime.strptime(fecha_str, "%Y-%m-%d").date()
        except ValueError:
            fecha = timezone.localdate()
    else:
        fecha = timezone.localdate()

    pedidos = Pedido.objects.filter(fecha_entrega__date=fecha).order_by("fecha_entrega")
    return render(request, "pedidos/agenda.html", {"pedidos": pedidos, "fecha": fecha})


@staff_member_required
def avanzar_estado(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == "POST":
        pedido.avanzar()
    fecha_str = request.POST.get("fecha", "")
    destino = reverse("agenda")
    if fecha_str:
        destino += f"?fecha={fecha_str}"
    return redirect(destino)

import subprocess
from django.http import HttpResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
@require_http_methods(["GET"])
def backup_db_view(request):
    """Ejecuta el script backup_db.py y devuelve un mensaje."""
    try:
        # Ruta absoluta al script (ya la sabemos)
        script_path = "/home/F4K3ll/Mi-Portafolio/Gestor-Pedidos-Goloso/backup_db.py"
        resultado = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True,
            cwd="/home/F4K3ll/Mi-Portafolio/Gestor-Pedidos-Goloso"
        )
        if resultado.returncode == 0:
            mensaje = "✅ " + resultado.stdout.strip()
            return HttpResponse(mensaje)
        else:
            error_msg = "❌ Error en el script: " + resultado.stderr.strip()
            return HttpResponse(error_msg, status=500)
    except Exception as e:
        return HttpResponse(f"Error inesperado: {e}", status=500)
