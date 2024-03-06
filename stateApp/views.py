from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import State
from django.urls import reverse_lazy
from .forms import StateModelForm
# Create your views here.

class StateCreateView(CreateView):
    model = State
    template_name = 'State_form.html'
    form_class = StateModelForm
    success_url = reverse_lazy('state_list')

 
class StateListView(ListView):
    model = State
    template_name = 'State_list.html'
    context_object_name = 'state_list'

class StateDetailView(DetailView):
    model = State
    template_name = 'State_detail.html'
    context_object_name = 'state'


class StateDeleteView(DeleteView):
    model = State
    template_name = 'State_confirm_delete.html'
    success_url = reverse_lazy('state_list')

class StateUpdateView(UpdateView):
    model = State
    template_name = "State_update_form.html"
    form_class = StateModelForm
    success_url = reverse_lazy('state_list')

    