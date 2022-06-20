from django.urls import path

from . import views

app_name = 'patients'
urlpatterns = [
    path('', views.index, name='index'),
    path('registrar-paciente/', views.register_patient),
    # path('pacientes/', views.list, name='list'),
    path('pacientes/', views.ListView.as_view(), name='list'),
    path('pacientes/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
