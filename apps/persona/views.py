from django.shortcuts import render

from django.views.generic import ListView,DetailView,CreateView
from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by = 15
    model = Empleado

class ListByAreaEmpleado(ListView):
    template_name = 'persona/list_by_area.html'
    
    def get_queryset(self):
        area = self.kwargs['shorname']       
        lista = Empleado.objects.filter(departamento__departamento=area)
        return lista

class ListEmpleadosByKword(ListView):
    """ Lista Empleado por palabra clave"""
    template_name = 'persona/by_kword.html'
    context_object_name = 'empleados'

    def get_queryset(self):       
        keyword = self.request.GET["kword"]
        lista = Empleado.objects.filter(
            first_name=keyword
        )       
        return lista


class ListHabilidadesEmpleado(ListView):
    template_name= 'persona/habilidades.html'
    context_object_name = 'habilidades'

    def get_queryset(self):
        empleado = Empleado.objects.get(id=6)      
        return empleado.habilidades.all()

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    
class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    fields = ('__all__')
    success_url = '.'


