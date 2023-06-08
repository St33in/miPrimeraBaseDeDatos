from Tools.demo.sortvisu import distinct
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404

from personas.models import Persona
from django.db.models import Q

# Create your views here.

def bienvenido(request):
    no_personas = Persona.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    # personas = Persona.objects.filter(id__contains=2)
    a = Persona.objects.all().aggregate(Sum('total'))
    a['total__sum'] += 1 -1

    # personas = Persona.objects.filter(nombre__startswith='J')
    busqueda = request.POST.get("buscar")

    if busqueda:
        personas = Persona.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(apellido__icontains=busqueda) |
            Q(ciudad__icontains=busqueda) |
            Q(numero__icontains=busqueda) |
            Q(no_domicilio__icontains=busqueda) |
            Q(calle__icontains=busqueda)




        ).distinct()


    return render(request,"bienvenido.html", {'no_personas': no_personas,'personas': personas,'a':a})

# def domicilios(request):
#     no_domicilios = Domicilio.objects.count()
#     domicilios = Domicilio.objects.order_by('-id')
#
#
#
#     return render(request,'domicilios.html',{'no_domicilios':no_domicilios,'domicilios':domicilios})

def filtro(request):
    personas = Persona.objects.order_by('id')
    # personas = Persona.objects.filter(id__contains=2)
    # a =  Persona.objects.all().aggregate(Sum('total'))
    # a['total__sum'] += 1
    # personas = Persona.objects.filter(nombre__startswith='J')
    busqueda = request.POST.get("buscar")

def principal(request):
    no_personas = Persona.objects.count()
    # personas = Persona.objects.all()
    personas = Persona.objects.order_by('id')
    a = Persona.objects.all().aggregate(Sum('total'))
    a ['total__sum' ]+= 1




    busqueda = request.POST.get("buscar")

    if busqueda:
        personas = Persona.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(apellido__icontains=busqueda) |
            Q(ciudad__icontains=busqueda) |
            Q(numero__icontains=busqueda) |
            Q(no_domicilio__icontains=busqueda) |
            Q(calle__icontains=busqueda)


        ).distinct()


    return render(request,'principal.html',{'no_personas':no_personas,'personas':personas,'a':a})






