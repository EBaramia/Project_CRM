import csv
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from .models import Client
from .forms import AddCommentForm, AddFileForm
from django.views.generic import CreateView, ListView, DeleteView, DetailView, UpdateView


class ClientsListView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_app/client_list.html'
    context_object_name = 'clients'

    def get_queryset(self):
        queryset = super(ClientsListView, self).get_queryset()
        return queryset.filter(
            created_by=self.request.user)


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client_app/client_detail.html'
    context_object_name = 'client'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AddCommentForm()
        context['fileform'] = AddFileForm()
        return context

    def get_queryset(self):
        queryset = super(ClientDetailView, self).get_queryset()
        return queryset.filter(
            created_by=self.request.user, pk=self.kwargs.get('pk'))


class AddFileView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        form = AddFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save(commit=False)
            file.team = self.request.user.userprofile.active_team
            file.client_id = pk
            file.created_by = request.user
            file.save()
        return redirect('client_app:clients_detail', pk=pk)


class AddCommentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        form = AddCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.team = self.request.user.userprofile.active_team
            comment.created_by = request.user
            comment.client_id = pk
            comment.save()
        return redirect('client_app:clients_detail', pk=pk)


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client
    template_name = 'lead/add_lead.html'
    fields = ('name', 'email', 'description', )
    success_url = reverse_lazy('client_app:clients_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        team = self.request.user.userprofile.active_team
        context['team'] = team
        context['title'] = 'Add client'
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.team = self.request.user.userprofile.active_team
        self.object.save()
        messages.success(self.request, 'The client was created.')

        return redirect(self.get_success_url())


class ClientsUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    template_name = 'client_app/client_edit.html'
    fields = ('name', 'email', 'description', )
    success_url = reverse_lazy('client_app:clients_list')

    def get_queryset(self):
        queryset = super(ClientsUpdateView, self).get_queryset()
        return queryset.filter(
            created_by=self.request.user, pk=self.kwargs.get('pk'))


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = reverse_lazy('client_app:clients_list')

    def get_queryset(self):
        queryset = super(ClientDeleteView, self).get_queryset()
        return queryset.filter(
            created_by=self.request.user, pk=self.kwargs.get('pk'))

    def post(self, request, *args, **kwargs):
        client = self.get_object()
        client.delete()
        return redirect(self.success_url)


@login_required
def clients_expotr(request):
    clients = Client.objects.filter(created_by=request.user)
    response = HttpResponse(
        content_type="text/csv",
        headers={"Content-Disposition": 'attachment; filename="clients.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(["Client", "Discription", "Created at", "Created by"])
    for client in clients:
        writer.writerow([client.name, client.description,
                        client.created_at, client.created_by])

    return response
