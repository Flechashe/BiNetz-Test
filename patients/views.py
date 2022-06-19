from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.template import loader

from .models import Patient

# Create your views here.

def index(request):
    return HttpResponse("Bienvenido al índice.")


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
