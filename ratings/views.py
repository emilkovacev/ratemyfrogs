from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Frog
from .forms import RatingForm

def index(request):
    if request.method == "POST":
        rating = 0
        if '1' in request.POST:
            rating = 1
        elif '2' in request.POST:
            rating = 2
        elif '3' in request.POST:
            rating = 3
        elif '4' in request.POST:
            rating = 4
        elif '5' in request.POST:
            rating = 5
        form = RatingForm(request.POST)
        if form.is_valid():
            id = form.cleaned_data['id']
            url = form.cleaned_data['url']
            Frog.objects.filter(id=id)
            old_frog
        return HttpResponseRedirect('/')
    allfrogs = Frog.objects.all()
    return render(request, 'ratings/index.html', {'id': allfrogs[0].id, 'url': allfrogs[0].url})
