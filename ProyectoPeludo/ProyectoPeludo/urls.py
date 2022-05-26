"""ProyectoPeludo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from ONG.views import bizcochito, blanquita, chocolate, chuchito, home, humberta, luchito
from ONG.views import gatos
from ONG.views import perros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home),
    path('home/gatos/',gatos),
    path('home/gatos/humberta',humberta),
    path('home/gatos/chuchito',chuchito),
    path('home/gatos/blanquita',blanquita),
    path('home/perros/',perros),
    path('home/perros/luchito',luchito),
    path('home/perros/bizcochito',bizcochito),
    path('home/perros/chocolate',chocolate),
]
