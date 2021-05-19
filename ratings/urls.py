from django.urls import path
from . import views

app_name = 'ratings'
urlpatterns = [
    path('', views.index, name='index')
]

