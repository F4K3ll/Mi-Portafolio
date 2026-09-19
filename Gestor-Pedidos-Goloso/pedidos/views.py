from datetime import datetime
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.http import require_http_methods
from .forms import PedidoForm
from .models import Pedido
from pathlib import Path
import subprocess

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


def avanzar_estado(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    if request.method == "POST":
        pedido.avanzar()
    fecha_str = request.POST.get("fecha", "")
    destino = reverse("agenda")
    if fecha_str:
        destino += f"?fecha={fecha_str}"
    return redirect(destino)


@require_http_methods(["GET"])
def backup_db_view(request):
    """Ejecuta el script backup_db.py usando Basic Auth."""
    # Autenticación básica HTTP desde el encabezado
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if not auth_header.startswith('Basic '):
        return HttpResponse('Autorización básica requerida', status=401,
                            content_type='text/plain')
    import base64
    try:
        encoded = auth_header[6:]  # quita 'Basic '
        decoded = base64.b64decode(encoded).decode('utf-8')
        username, password = decoded.split(':', 1)
    except Exception:
        return HttpResponse('Credenciales inválidas', status=401,
                            content_type='text/plain')

    # Autenticar usando Django
    user = authenticate(request, username=username, password=password)
    if user is None or not user.is_staff:
        return HttpResponse('Acceso denegado', status=403,
                            content_type='text/plain')

    # Ejecutar el script
    BASE_DIR = Path(__file__).resolve().parent.parent
    script_path = str(BASE_DIR / "backup_db.py")
    try:
        resultado = subprocess.run(
            ["python", script_path],
            capture_output=True,
            text=True,
            cwd=str(BASE_DIR)
        )
        if resultado.returncode == 0:
            mensaje = "✅ " + resultado.stdout.strip()
            return HttpResponse(mensaje)
        else:
            return HttpResponse("❌ Error: " + resultado.stderr.strip(),
                                status=500)
    except Exception as e:
        return HttpResponse(f"Error: {e}", status=500)
