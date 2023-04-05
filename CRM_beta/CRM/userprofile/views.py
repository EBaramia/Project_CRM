from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('userprofile:login')
    else:
        form = UserCreationForm()
    return render(request, 'userprofile/signup_page.html', {'form': form})
