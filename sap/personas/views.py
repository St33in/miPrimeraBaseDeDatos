from django.shortcuts import render, get_object_or_404, redirect

from personas.forms import FormaPersona
from personas.models import Persona


# Create your views here.


def mostrar_detalle(request, id):
    persona = get_object_or_404(Persona, pk=id)

    return render(request, 'detalle.html', {'persona': persona})


def NuevaPersona(request):
    if request.method == 'POST':
        formapersona = FormaPersona(request.POST)
        if formapersona.is_valid():
            formapersona.save()
            return redirect("bienvenido")

    else:
        formapersona = FormaPersona()

    return render(request, 'nuevapersona.html', {'formapersona': formapersona})


def EditarPersona(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if request.method == 'POST':
        formapersona = FormaPersona(request.POST, instance=persona)
        if formapersona.is_valid():
            formapersona.save()
            return redirect('bienvenido')

    else:

        persona = get_object_or_404(Persona, pk=id)
        formapersona = FormaPersona(instance=persona)

    return render(request, 'editarpersona.html', {'formapersona': formapersona})


def eliminar(request, id):
    persona = get_object_or_404(Persona, pk=id)
    if persona:
        persona.delete()
    return redirect('bienvenido')
# def detalle_domicilio(request, id):
#     domicilios = get_object_or_404(Domicilio, pk=id)
#
#     return render(request, 'detalle_domicilio.html', {'domicilios': domicilios})
#
#
# def agregar_domicilio(request):
#     if request.method == 'POST':
#         forma = FormaDomicilio(request.POST)
#         if forma.is_valid():
#             forma.save()
#             return redirect('domicilios')
#
#     else:
#         forma = FormaDomicilio()
#
#     return render(request, 'agregar_domicilio.html', {'forma': forma})
#
#
# def editar_domicilio(request, id):
#     domicilios = get_object_or_404(Domicilio, pk=id)
#     if request.method == 'POST':
#         forma = FormaDomicilio(request.POST, instance=domicilios)
#         if forma.is_valid():
#             forma.save()
#             return redirect('domicilios')
#     else:
#         domicilios = get_object_or_404(Domicilio, pk=id)
#         forma = FormaDomicilio(instance=domicilios)
#
#     return render(request, 'editar_domicilio.html', {'forma': forma})
#
#
# def eliminarDomicilio(request, id):
#     domicilios = get_object_or_404(Domicilio, pk=id)
#     if domicilios:
#         domicilios.delete()
#     return redirect('domicilios')
#

