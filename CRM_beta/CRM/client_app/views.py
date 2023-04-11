from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from team.models import Team
from django.views import View
from .models import Client
from .forms import AddCommentForm
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView


class ClientsListView(ListView):
    model = Client
    template_name = 'client_app/client_list.html'
    context_object_name = 'clients'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super(ClientsListView, self).get_queryset()
        return queryset.filter(
            created_by=self.request.user)


class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_app/client_detail.html'
    context_object_name = 'client'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddCommentForm()
        return context

    def get_queryset(self):
        queryset = super(ClientDetailView, self).get_queryset()
        return queryset.filter(
            created_by=self.request.user, pk=self.kwargs.get('pk'))


class AddCommentView(View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        form = AddCommentForm(request.POST)
        if form.is_valid():
            team = Team.objects.filter(created_by=self.request.user)[0]
            comment = form.save(commit=False)
            comment.team = team
            comment.created_by = request.user
            comment.client_id = pk
            comment.save()
        return redirect('client_app:clients_detail', pk=pk)


class ClientCreateView(CreateView):
    model = Client
    template_name = 'lead/add_lead.html'
    fields = ('name', 'email', 'description', )
    success_url = reverse_lazy('client_app:clients_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = Team.objects.filter(created_by=self.request.user)[0]
        context['team'] = team
        context['title'] = 'Add client'
        return context

    def form_valid(self, form):
        team = Team.objects.filter(created_by=self.request.user)[0]
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.team = team
        self.object.save()
        messages.success(self.request, 'The client was created.')

        return redirect(self.get_success_url())


class ClientsUpdateView(UpdateView):
    model = Client
    template_name = 'client_app/client_edit.html'
    fields = ('name', 'email', 'description', )
    success_url = reverse_lazy('client_app:clients_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super(ClientsUpdateView, self).get_queryset()
        return queryset.filter(
            created_by=self.request.user, pk=self.kwargs.get('pk'))


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('client_app:clients_list')

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        queryset = super(ClientDeleteView, self).get_queryset()
        return queryset.filter(
            created_by=self.request.user, pk=self.kwargs.get('pk'))

    def post(self, request, *args, **kwargs):
        client = self.get_object()
        client.delete()
        return redirect(self.success_url)
