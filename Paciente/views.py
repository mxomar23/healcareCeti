from datetime import datetime

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.template.context_processors import request
from django.urls import reverse_lazy, reverse
from .PythonApp import agregar, buscar
from .forms import *
from django.shortcuts import render, redirect
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView
)


class PacienteListView(ListView):
    template_name = 'paciente/lista.html'
    queryset = Paciente.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        context = {
            'object_list': self.get_queryset(),
            'title': 'Lista de pacientes',
            'year': datetime.now().year,
        }
        return render(request, self.template_name, context)


class PacienteDetailView(DetailView):
    template_name = 'paciente/perfil.html'
    model = Paciente

    def get_context_data(self, queryset=None, *args, **kwargs):
        context = super(PacienteDetailView, self).get_context_data(**kwargs)
        _id = self.kwargs.get("pk")
        context['id'] = _id
        queryset = Paciente.objects.filter(id=_id)
        aler = []
        for a in queryset:
            aler = a.alergias.values('nombre')
        context["object"] = queryset
        context['alergias'] = aler
        context['year'] = datetime.now().year
        context['title'] = 'Detalles del paciente'
        return context


def agregar_paciente(request, *args, **kwargs):

    if agregar(kwargs['pk']):
        messages.success(request, 'Se agregó correctamente')
        return HttpResponseRedirect(reverse('pacientes:paciente-lista'))
    else:
        messages.error(request, 'Hubo un error.')
        return HttpResponseRedirect(reverse('pacientes:paciente-lista'))


def index(request):
    template = 'paciente/index.html'
    context = {
        'title': 'Buscar paciente',
        'year': datetime.now().year,
    }
    return render(request, template, context)


def buscar_paciente(request):
    id_paciente = buscar()
    if id_paciente:
        messages.success(request, 'Se encontró correctamente')
        return HttpResponseRedirect(reverse('pacientes:paciente-perfil', args=(id_paciente,)))
    else:
        messages.error(request, 'Hubo un error.')
        return HttpResponseRedirect(reverse('pacientes:paciente-lista'))