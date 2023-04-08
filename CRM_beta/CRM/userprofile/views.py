from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile
from team.models import Team


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            team = Team.objects.create(
                name='The team name', created_by=request.user)
            team.members.add(request.user)
            team.save()
            return redirect('userprofile:login')
    else:
        form = UserCreationForm()
    return render(request, 'userprofile/signup_page.html', {'form': form})


@login_required
def my_account(request):
    team = Team.objects.filter(created_by=request.user)[0]
    return render(request, 'userprofile/account.html', {'team': team})
