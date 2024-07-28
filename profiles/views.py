from django.shortcuts import render
from django.http import JsonResponse

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
