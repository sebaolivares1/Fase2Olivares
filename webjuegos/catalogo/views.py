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

def tuDestiny(request):
    
    return render(
        request,
        'tuDestiny.html',
    )

def tuSea(request):
    
    return render(
        request,
        'tuSea.html',
    )

def videos(request):
    
    return render(
        request,
        'videos.html',
    )
def agjuegos(request):
    
    return render(
        request,
        'agjuegos.html',
    )


from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


#views

class JuegoCreate(CreateView):
    model = Juego
    fields = '__all__'

class JuegoUpdate(UpdateView):
    model = Juego
    fields = '__all__'

class JuegoDelete(DeleteView):
    model = Juego
    success_url = reverse_lazy('index')

class JuegoDetailView(generic.DetailView):
    model = Juego


class JuegoListView(generic.ListView):
    model = Juego
    paginate_by = 6