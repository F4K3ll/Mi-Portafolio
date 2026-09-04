from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PedidoForm


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