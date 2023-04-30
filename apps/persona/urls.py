from django.urls import path

from .views import ListAllEmpleados,ListByAreaEmpleado,ListEmpleadosByKword,ListHabilidadesEmpleado,EmpleadoCreateView


urlpatterns = [
    path('lista_empleados', ListAllEmpleados.as_view()),
    path('lista_by_area/<shorname>', ListByAreaEmpleado.as_view()),
    path('buscar-empleado/', ListEmpleadosByKword.as_view()),
    path('lista-habilidades-empleado/', ListHabilidadesEmpleado.as_view()),
    path('add-empleado/', EmpleadoCreateView.as_view()),
]
