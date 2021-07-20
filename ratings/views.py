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
        if request.session['unrated_frog_urls']: 
            request.session['current_frog_url'] = secrets.choice(request.session['unrated_frog_urls'])
        else:
            request.session['current_frog_url'] = ''
        return HttpResponseRedirect('/')
    def bayesianAverage(frog):
        if frog.avg == 0:
            return frog.avg
        else:
            ((frog.total + (10 * 3)) / (frog.n + 10))
    top_frogs = sorted(list(Frog.objects.all()), key=bayesianAverage, reverse=True)[:10]    
    if request.session['unrated_frog_urls']:
        return render(request, 'ratings/index.html', 
            {
                'url': request.session['current_frog_url'], 
                'top_frogs': top_frogs, 
                'appearance': request.COOKIES.get('appearance')
            })
    else:
        return render(request, 'ratings/index.html', 
            {
                'url': request.session['current_frog_url'], 
                'top_frogs': top_frogs, 
                'appearance': request.COOKIES.get('appearance')
            })

