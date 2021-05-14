from django.shortcuts import render
from .models import Frog

def index(request):
    allfrogs = Frog.objects.all()
    print(allfrogs[0].frog)
    return render(request, 'ratings/index.html', {'frog': allfrogs[0].frog})
