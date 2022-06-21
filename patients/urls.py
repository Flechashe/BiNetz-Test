from django.urls import path

from . import views

app_name = 'patients'
urlpatterns = [
    path('', views.index, name='index'),
    path('registrar-paciente/', views.process_register_patient),
    path('editar-paciente/<int:pk>/', views.edit_patient),
    path('procesar-edicion/<int:pk>', views.process_edit_patient),
    path('eliminar-paciente/<int:pk>/', views.delete_patient),

    # 🢃 Estas URLs fueron un primer approach, después cambié el rumbo y las abandoné.
    # path('pacientes/', views.list, name='list'),
    path('pacientes/', views.ListView.as_view(), name='list'),
    path('pacientes/<int:pk>/', views.DetailView.as_view(), name='detail'),
]
