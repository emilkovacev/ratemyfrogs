from django.shortcuts import render
from django.http import HttpResponseRedirect
import secrets
from .models import Frog
from .forms import RatingForm

def index(request):
    if 'unrated_frog_urls' not in request.session:
        request.session['unrated_frog_urls'] = [frog.url for frog in Frog.objects.all()]
        request.session['current_frog_url'] = request.session['unrated_frog_urls'][0]

    if request.method == "POST":
        rating = 0
        notfrog = False
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
        elif '0' in request.POST:
            notfrog = True
        
        form = RatingForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            request.session[url] = True
            froggy = Frog.objects.get(pk = url)
            if not notfrog:
                froggy.n += 1
                froggy.total = froggy.total + rating
            else:
                # notfrogs does not increment n or total;
                # % notfrogs = (n + notfrogs) / (total + notfrogs)
                froggy.notfrogs += 1
            froggy.save()

        request.session['unrated_frog_urls'].remove(url)
        request.session['current_frog_url'] = secrets.choice(request.session['unrated_frog_urls'])
        return HttpResponseRedirect('/')
    
    if request.session['unrated_frog_urls']:
        return render(request, 'ratings/index.html', {'url': request.session['current_frog_url'], 'frogstring': ''})
