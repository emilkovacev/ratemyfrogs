from django.shortcuts import render
from django.http import HttpResponseRedirect
import random
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
            url = form.cleaned_data['url']
            request.session[url] = True
            print('form recieved')
        return HttpResponseRedirect('/')
    
    allfrogs = Frog.objects.all()
    unratedfrogs = []
    for frog in allfrogs:
        if str(frog.url) not in request.session:
            request.session[str(frog.url)] = False
        if request.session[str(frog.url)] == False:
            unratedfrogs.append(frog)
    thisfrog = unratedfrogs[random.randint(0, len(unratedfrogs)-1)]
    if allfrogs:
        return render(request, 'ratings/index.html', {'frog': thisfrog.url})
    else:
        return render(request, 'ratings/index.html', {'frog': ''})
