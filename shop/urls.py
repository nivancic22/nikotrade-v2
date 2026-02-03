from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('katalog/', views.katalog, name='katalog'),
    path('proizvod/<int:id>/', views.detalji_proizvoda, name='detalji_proizvoda'), 
    path('kontakt/', views.kontakt, name='kontakt'),  
]
