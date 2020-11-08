from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('juego/<int:pk>', views.JuegoDetailView.as_view(), name='juego-detail'),
    path('juegos/', views.JuegoListView.as_view(), name='juegos'),
]

urlpatterns+=[
    path('juego/create/', views.JuegoCreate.as_view(), name='juego_create'),
    path('juego/<int:pk>/update/', views.JuegoUpdate.as_view(), name='juego_update'),
    path('juego/<int:pk>/delete/', views.JuegoDelete.as_view(), name='juego_delete'),
    

]