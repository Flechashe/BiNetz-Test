from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.template import loader

from .models import Patient

# Create your views here.


def index(request):
    patients = Patient.objects.all()
    return render(request, 'patients/index.html', {'patients': patients})


def process_register_patient(request):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    dni = request.POST['dni']
    sexo = request.POST['sexo']
    email = request.POST['email']
    fecha_de_nacimiento = request.POST['fecha_de_nacimiento']
    cobertura_medica = request.POST['cobertura_medica']

    patient = Patient.objects.create(nombre=nombre, apellido=apellido, dni=dni, sexo=sexo,
                                     email=email, fecha_de_nacimiento=fecha_de_nacimiento, cobertura_medica=cobertura_medica)
    return redirect('/')


def edit_patient(request, pk):
    patient_to_edit = Patient.objects.get(id=pk)
    return render(request, 'patients/edit_patient.html', {'patient': patient_to_edit})


def process_edit_patient(request, pk):
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    dni = request.POST['dni']
    sexo = request.POST['sexo']
    email = request.POST['email']
    fecha_de_nacimiento = request.POST['fecha_de_nacimiento']
    cobertura_medica = request.POST['cobertura_medica']

    patient_to_edit = Patient.objects.get(id=pk)
    patient_to_edit.nombre = nombre
    patient_to_edit.apellido = apellido
    patient_to_edit.dni = dni
    patient_to_edit.sexo = sexo
    patient_to_edit.email = email
    patient_to_edit.fecha_de_nacimiento = fecha_de_nacimiento
    patient_to_edit.cobertura_medica = cobertura_medica
    patient_to_edit.save()
    return redirect('/')


def delete_patient(request, pk):
    patient_to_delete = Patient.objects.get(id=pk)
    patient_to_delete.delete()
    return redirect('/')


# def list(request):
#     patient_list = Patient.objects.all()
#     template = loader.get_template('patients/patient_list.html')
#     context = {
#         'patient_list': patient_list,
#     }
#     return HttpResponse(template.render(context, request))


class ListView(generic.ListView):
    model = Patient


class DetailView(generic.DetailView):
    model = Patient
