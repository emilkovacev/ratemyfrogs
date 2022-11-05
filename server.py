from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse, PlainTextResponse

from db import *
import os
import random
import csv
import io


templates = Jinja2Templates(directory='templates')
development = True

def get_host():
    if development:
        return 'http://0.0.0.0:5003'
    else:
        return 'https://ratemyfrogs.com'

async def homepage(request):    
    if 'current_frog' in request.cookies:
        frog_img = request.cookies.get('current_frog')
    else:
        frog_img = get_random_frog()

    response = templates.TemplateResponse('index.html', {
        'request': request,
        'frog': {
            'name': 'frog',
            'url': f'{get_host()}/frogs/{frog_img}', 
        },
        'most_popular': get_most_popular()
    })

    response.set_cookie('current_frog', frog_img)

    return response
  

async def rate(request):
    form = await request.form()
    url, rating = form['url'], form['rating']
    if rating != 'not a frog':
        rating = int(rating)
        increment_frog(url, rating)
    response = RedirectResponse(url='/')
    new_frog = get_random_frog()
    response.set_cookie('current_frog', new_frog)

    # change current frog cookie
    return response


# search for a unique, randomly generated frog
def get_random_frog(rated=None):
    try:
        frogs = os.listdir('./frogs')
        while True:
            i = random.randint(0, len(frogs) - 1)
            random_frog = frogs[i]
            if not rated or random_frog not in rated:
                break
        return random_frog

    except FileExistsError:
        return 'error 500, server has not been properly initialized! (run ./run_server)'



async def csv_data(request):
    data = get_frogs()
    headers = ['_id', 'url', 'n', 'total', 'avg']
    string = io.StringIO()
    writer = csv.DictWriter(string, headers)

    writer.writeheader()
    for elem in data:
        writer.writerow(elem)

    response = PlainTextResponse(string.getvalue())
    return response



app = Starlette(debug=True, routes=[
    Route('/', homepage, methods=['GET', 'POST']),
    Route('/rate', rate, methods=['POST']),
    Mount('/static', StaticFiles(directory='static'), name='static'),
    Mount('/frogs', StaticFiles(directory='frogs'), name='frogs'),
    Route('/data', csv_data)
])
