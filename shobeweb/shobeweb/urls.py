"""shobeweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings
from django.contrib import admin
from inventario.views import *

from django.urls import path, re_path
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^$', home, name='home'),
    re_path(r'^productos',productos, name='productos'),
    re_path(r'^ventas',ventas, name='ventas'),
    re_path(r'^detalleventa/(?P<idventa>\d+)$',detalleventa, name='detalleventa'),
    re_path(r'^ventadiaria',ventadiaria, name='ventadiaria'),
]
