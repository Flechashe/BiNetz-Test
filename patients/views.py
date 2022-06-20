from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.template import loader

from .models import Patient

# Create your views here.


def index(request):
    patients = Patient.objects.all()
    return render(request, 'patients/index.html', {'patients': patients})


def register_patient(request):
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
