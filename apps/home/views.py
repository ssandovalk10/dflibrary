from django.shortcuts import render
from django.views.generic import TemplateView, ListView


class IndexView(TemplateView):
    template_name = "home/index.html"


class PruebaListView(ListView):
    template_name = "home/lista.html"
    queryset = ['A', 'B', 'C']
    context_object_name = 'lista_prueba'

