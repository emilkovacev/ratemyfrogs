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
        print(rating)
        form = RatingForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            print('form recieved')
        return HttpResponseRedirect('/')
    allfrogs = Frog.objects.all()
    print(allfrogs[0].frog)
    return render(request, 'ratings/index.html', {'frog': allfrogs[0].frog})
