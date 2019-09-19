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