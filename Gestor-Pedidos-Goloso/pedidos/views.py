from datetime import datetime

from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.utils import timezone

from .forms import PedidoForm
from .models import Pedido


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