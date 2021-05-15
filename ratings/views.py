from django.shortcuts import render
from .models import Frog

def index(request):
    allfrogs = Frog.objects.all()
    if allfrogs:
        return render(request, 'ratings/index.html', {'frog': allfrogs[0].url})
    else:
        return render(request, 'ratings/index.html', {'frog': ''})
