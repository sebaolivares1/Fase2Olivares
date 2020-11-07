from django.shortcuts import render
from . models import Juego, JuegoInstance
from django.views import generic


# Create your views here.
def index(request):
    num_Juegos = Juego.objects.all().count()
    num_Instances = JuegoInstance.objects.all().count()
    
    return render(
        request,
        'index.html',
        context={'num_juegos': num_Juegos, 'num_instances': num_Instances,},
    )