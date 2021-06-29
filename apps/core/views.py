from apps.userprofile.models import Userprofile
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def frontpage(request):
    return render(request, "core/frontpage.html")

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            Userprofile.objects.create(user=user)

            return redirect("frontpage")
    else:
        form = UserCreationForm()

    return render(request, "core/signup.html", {"form": form})

def plans(request):
    return render(request, "core/plans.html")