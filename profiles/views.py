from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse

from .models import Profile


def index(request):
    """Home page"""
    return render(request, "profile/index.xhtml")

def get_profiles(request):
    """Get all the profiles from the database"""
    profiles = Profile.objects.all().order_by("id")

    context = {
        "profiles": list(profiles.values())
    }

    return JsonResponse(context)

def create_profile(request):
    if request.method == "POST" and request.POST.get("action") == "post":
        data = request.POST
        print(data)
        name = data["name"]
        email = data["email"]
        bio = data["bio"]
        new_profile = Profile(name=name, email=email, bio=bio)
        new_profile.save()

        return HttpResponse()