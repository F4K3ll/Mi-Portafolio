# config/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pedidos/', include('pedidos.urls')),

    # Redirige la raíz (/) a la agenda
    path('', RedirectView.as_view(url='/pedidos/agenda/', permanent=False)),
]