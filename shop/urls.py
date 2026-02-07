from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('katalog/', views.katalog, name='katalog'),
    path('proizvod/<int:id>/', views.detalji_proizvoda, name='detalji'), 
    path('kontakt/', views.kontakt, name='kontakt'),  
    path('proizvod/<int:proizvod_id>/upit/', views.posalji_upit, name='posalji_upit'),
    path('kontakt/posalji/', views.posalji_kontakt_upit, name='posalji_kontakt_upit'),
    path('politika-privatnosti/', views.politika_privatnosti, name='politika_privatnosti'),
]
