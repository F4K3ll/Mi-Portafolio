from django.core.exceptions import ValidationError
from django.utils import timezone
from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    TIPO_CHOICES = [
        ("helado", "Helado"),
        ("postre", "Postre"),
    ]
    sabor = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default="helado")

    def __str__(self):
        return f"{self.sabor} ({self.get_tipo_display()})"


class Pedido(models.Model):
    CANTIDAD_CHOICES = [
        ("cuarto", "1/4 kg"),
        ("medio", "1/2 kg"),
        ("kilo", "1 kg"),
    ]
    ESTADO_CHOICES = [
        ("pendiente", "Pendiente"),
        ("listo", "Listo"),
        ("entregado", "Entregado"),
    ]
    SIGUIENTE_ESTADO = {
        "pendiente": "listo",
        "listo": "entregado",
    }

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=10, choices=CANTIDAD_CHOICES)
    fecha_entrega = models.DateTimeField()
    estado = models.CharField(max_length=10, choices=ESTADO_CHOICES, default="pendiente")

    def clean(self):
        if self.fecha_entrega and self.fecha_entrega < timezone.now():
            raise ValidationError("La fecha de entrega no puede ser en el pasado.")

    def avanzar(self):
        """Mueve el pedido al siguiente estado, si corresponde. Devuelve True si cambió."""
        siguiente = self.SIGUIENTE_ESTADO.get(self.estado)
        if siguiente:
            self.estado = siguiente
            self.save()
            return True
        return False

    def siguiente_estado_label(self):
        siguiente = self.SIGUIENTE_ESTADO.get(self.estado)
        if not siguiente:
            return None
        return dict(self.ESTADO_CHOICES).get(siguiente)

    def __str__(self):
        return f"Pedido de {self.cliente} - {self.producto} ({self.get_cantidad_display()})"