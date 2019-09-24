# coding=utf-8
from django.shortcuts import render, get_object_or_404,redirect,get_list_or_404,render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.template.loader import get_template
from django.template import Context
from django.template.context import RequestContext
from django.core import serializers
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
#from .forms import *
from django.views.generic import TemplateView, FormView,CreateView, UpdateView
#from django.core.urlresolvers import reverse_lazy, reverse
from .models import *
from random import choice
#from eres.metodos import *
from decimal import Decimal
from datetime import datetime,timedelta
import time
import hashlib
from django.utils import timezone
import pytz
from django.core.mail import EmailMessage
from django.db.models import Q
#from .htmltopdf import render_to_pdf
from datetime import *
from django.template.defaultfilters import slugify
import sys



# Create your views here.

def productos(request):
    
    template = "productos.html"
    saludo = "Esta es la pagina de productos que es una variable"
    pro = Productos.objects.all()



    context = {'saludo':saludo,'pr':pro}

    return render(request,template,context)


def ventas(request):
    
    template = "ventas.html"
    saludo = "aqui van ha ir la ventas"

    hoy = datetime.today()
    dia = datetime.today().day
    mes = datetime.now().month
    year = datetime.now().year
    semana = datetime.now().weekday()

    numventas = Facturaventa.objects.filter(fecha__month=mes,fecha__year=2018).order_by('codfacturav').count()
    #ventas = Facturaventa.objects.filter(fecha__month=mes,fecha__year=2018).order_by('codfacturav')[(numventas/2):numventas]
    ventas = Facturaventa.objects.filter(fecha__range=('2019-08-04', '2019-08-04')).order_by('codfacturav').reverse()
    

    lventas = []

    class Nventas:
        condfacturav = 0
        numfacturav = 0
        cliente = ''
        tipo = ''
        fecha = ''
        usuario = ''
        total = 0
        nula = True

    cl = ''
    for x in ventas:
        nv = Nventas()
        nv.codfacturav = x.codfacturav
        nv.numfacturav = x.numfacturav


        try:
            cl = Cliente.objects.get(codcliente_id = x.codcliente)
        except Exception as e:
            print("Ocurrio un error con el cliente")
            print(x.codcliente)
            print(x.numfacturav)
        
        
        
    
        nv.cliente = cl.nombre
        nv.tipo = x.tipo
        nv.fecha = x.fecha
        nv.usuario = x.usuario
        nv.total = x.total

        if x.estado == 'invalida':
            nv.nula = False
            

        lventas.append(nv)
    
   

        

     

  
    #Model.objects.filter(fecha__month = mes)

    context = {'saludo':saludo,'vent':lventas,'hoy':hoy}

    return render(request,template,context)


def detalleventa(request,idventa):
    
    template = "detalleventa.html"
    saludo = "aqui van a ir el detalle de la venta"
    venta = Facturaventa.objects.get(codfacturav = idventa)
    cliente = Cliente.objects.get(codcliente_id = venta.codcliente)

    deta = Detalleventa.objects.filter(codfacturav = venta.codfacturav)

    class Facturav:
        cliente = ''
        nit = ''
        nrc = ''
        numfactura = ''
        tiraje = ''
        tipo = ''
        fpago = ''
        fecha = ''

    f = Facturav()

    f.cliente = cliente.nombre
    f.nit =  cliente.nit 
    f.nrc = cliente.nrc
    f.numfactura = venta.numfacturav
    f.tiraje = venta.tiraje
    f.tipo = venta.tipo
    f.fpago = venta.formadepago

    class Odetalle:
        codigo = ''
        cantidad = 0
        producto = 0
        codproducto = ''
        preciounitario = 0
        ventasafectas = 0
    
    detalle = []
    pr = []

    for x in deta:
        o = Odetalle()
        o.codigo = x.coddetallefacturav
        o.cantidad = x.cantidadunit
        pr = Productos.objects.get(codproducto = x.codproducto)
        o.producto = pr.nombre
        o.codproducto = x.codproducto
        o.preciounitario = x.preciopublico
        o.ventasafectas = x.total

        detalle.append(o)
    



    context = {'detalle':detalle,'f':f,'fa':venta}

    return render(request,template,context)




def ventadiaria(request):
    
    template = "ventadiaria.html"
    saludo = "Venta diaria"
    



    context = {'saludo':saludo}

    return render(request,template,context)