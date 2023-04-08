from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from lead.models import Lead
from client_app.models import Client
from team.models import Team


@login_required
def dachboard(request):
    team = Team.objects.filter(created_by=request.user)[0]
    leads = Lead.objects.filter(
        team=team, converted_to_client=False).order_by('-created_at')[0:5]
    clients = Client.objects.filter(team=team).order_by('-created_at')[0:5]
    return render(request, 'dashboard/dashboard.html', {
        'leads': leads,
        'clients': clients,
    })
