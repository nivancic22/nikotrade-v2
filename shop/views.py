from django.shortcuts import render
from .models import Proizvod  

def index(request):
    return render(request, 'shop/index.html')

def katalog(request):
    kategorija_slug = request.GET.get('kategorija')
    
    if kategorija_slug:
        proizvodi_iz_baze = Proizvod.objects.filter(kategorija=kategorija_slug)
    else:
        proizvodi_iz_baze = Proizvod.objects.all()
    
    return render(request, 'shop/katalog.html', {'proizvodi': proizvodi_iz_baze})

def kontakt(request):
    return render(request, 'shop/kontakt.html')