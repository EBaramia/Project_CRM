from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from .forms import SingUpForm
from team.models import Team


def signup(request):
    if request.method == 'POST':
        form = SingUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            team = Team.objects.create(
                name='The team name', created_by=request.user)
            team.members.add(request.user)
            team.save()
            UserProfile.objects.create(
                user=user, active_team=team)
            return redirect('userprofile:login')
    else:
        form = SingUpForm()
    return render(request, 'userprofile/signup_page.html', {'form': form})


@login_required
def my_account(request):
    return render(request, 'userprofile/account.html')
