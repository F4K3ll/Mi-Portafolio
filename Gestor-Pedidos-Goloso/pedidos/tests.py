from datetime import timedelta

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Cliente, Pedido, Producto


class PedidoModelTests(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre="Ana", telefono="1122334455")
        self.producto = Producto.objects.create(sabor="Dulce de leche", tipo="helado")

    def test_fecha_futura_es_valida(self):
        pedido = Pedido(
            cliente=self.cliente,
            producto=self.producto,
            cantidad="medio",
            fecha_entrega=timezone.now() + timedelta(days=1),
        )
        pedido.full_clean()

    def test_fecha_pasada_es_invalida(self):
        pedido = Pedido(
            cliente=self.cliente,
            producto=self.producto,
            cantidad="medio",
            fecha_entrega=timezone.now() - timedelta(days=1),
        )
        with self.assertRaises(ValidationError):
            pedido.full_clean()

    def test_avanzar_cambia_los_estados_en_orden(self):
        pedido = Pedido.objects.create(
            cliente=self.cliente,
            producto=self.producto,
            cantidad="kilo",
            fecha_entrega=timezone.now() + timedelta(hours=1),
        )
        self.assertEqual(pedido.estado, "pendiente")
        pedido.avanzar()
        self.assertEqual(pedido.estado, "listo")
        pedido.avanzar()
        self.assertEqual(pedido.estado, "entregado")

    def test_avanzar_no_hace_nada_si_ya_esta_entregado(self):
        pedido = Pedido.objects.create(
            cliente=self.cliente,
            producto=self.producto,
            cantidad="kilo",
            fecha_entrega=timezone.now() + timedelta(hours=1),
            estado="entregado",
        )
        cambio = pedido.avanzar()
        self.assertFalse(cambio)
        self.assertEqual(pedido.estado, "entregado")


class VistasPedidoTests(TestCase):
    def setUp(self):
        self.cliente = Cliente.objects.create(nombre="Ana", telefono="1122334455")
        self.producto = Producto.objects.create(sabor="Dulce de leche", tipo="helado")
        self.usuario = get_user_model().objects.create_user(
            username="personal_prueba",
            is_staff=True,
        )
        self.client.force_login(self.usuario)

    def test_formulario_crea_pedido_con_fecha_futura(self):
        fecha = (timezone.now() + timedelta(days=1)).strftime("%Y-%m-%dT%H:%M")
        response = self.client.post(reverse("nuevo_pedido"), {
            "cliente": self.cliente.id,
            "producto": self.producto.id,
            "cantidad": "medio",
            "fecha_entrega": fecha,
            "estado": "pendiente",
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Pedido.objects.count(), 1)

    def test_formulario_rechaza_fecha_pasada(self):
        fecha = (timezone.now() - timedelta(days=1)).strftime("%Y-%m-%dT%H:%M")
        response = self.client.post(reverse("nuevo_pedido"), {
            "cliente": self.cliente.id,
            "producto": self.producto.id,
            "cantidad": "medio",
            "fecha_entrega": fecha,
            "estado": "pendiente",
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Pedido.objects.count(), 0)

    def test_agenda_muestra_pedidos_del_dia_elegido(self):
        hoy = timezone.localdate()
        Pedido.objects.create(
            cliente=self.cliente, producto=self.producto, cantidad="cuarto",
            fecha_entrega=timezone.now() + timedelta(hours=1),
        )
        response = self.client.get(reverse("agenda"), {"fecha": hoy.strftime("%Y-%m-%d")})
        self.assertContains(response, "Ana")

    def test_avanzar_estado_desde_la_vista(self):
        pedido = Pedido.objects.create(
            cliente=self.cliente, producto=self.producto, cantidad="cuarto",
            fecha_entrega=timezone.now() + timedelta(hours=1),
        )
        self.client.post(reverse("avanzar_estado", args=[pedido.id]), {"fecha": ""})
        pedido.refresh_from_db()
        self.assertEqual(pedido.estado, "listo")

    def test_bloquea_acceso_sin_permiso_staff(self):
        usuario_comun = get_user_model().objects.create_user(
            username="usuario_comun",
            is_staff=False,
        )
        fecha = timezone.now() + timedelta(days=1)
        pedido = Pedido.objects.create(
            cliente=self.cliente,
            producto=self.producto,
            cantidad="cuarto",
            fecha_entrega=fecha,
        )
        datos = {
            "cliente": self.cliente.id,
            "producto": self.producto.id,
            "cantidad": "medio",
            "fecha_entrega": timezone.localtime(fecha).strftime("%Y-%m-%dT%H:%M"),
            "estado": "pendiente",
        }
        casos = [
            ("get", reverse("agenda"), {}),
            ("get", reverse("nuevo_pedido"), {}),
            ("post", reverse("nuevo_pedido"), datos),
            ("post", reverse("avanzar_estado", args=[pedido.id]), {"fecha": ""}),
        ]

        for usuario in (None, usuario_comun):
            self.client.logout()
            if usuario is not None:
                self.client.force_login(usuario)

            for metodo, url, contenido in casos:
                with self.subTest(
                    usuario="anonimo" if usuario is None else usuario.username,
                    metodo=metodo,
                    url=url,
                ):
                    response = getattr(self.client, metodo)(url, contenido)
                    self.assertRedirects(
                        response,
                        f"{reverse('admin:login')}?next={url}",
                        fetch_redirect_response=False,
                    )
                    self.assertEqual(Pedido.objects.count(), 1)
                    pedido.refresh_from_db()
                    self.assertEqual(pedido.estado, "pendiente")
