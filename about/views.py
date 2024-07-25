from django.shortcuts import render
from .models import About

# Create your views here.
def about(request):
    """
    Display the latest About content
    """
    latest_about = About.objects.all().order_by("-updated_on").first()

    return render(
        request,
        "about/about.html",
        {"latest_about": latest_about},
    )
