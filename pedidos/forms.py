from django import forms
from .models import Pedido


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ["cliente", "producto", "cantidad", "fecha_entrega", "estado"]
        widgets = {
            "fecha_entrega": forms.DateTimeInput(
                attrs={"type": "datetime-local", "class": "form-control"}
            ),
            "cliente": forms.Select(attrs={"class": "form-select"}),
            "producto": forms.Select(attrs={"class": "form-select"}),
            "cantidad": forms.Select(attrs={"class": "form-select"}),
            "estado": forms.Select(attrs={"class": "form-select"}),
        }