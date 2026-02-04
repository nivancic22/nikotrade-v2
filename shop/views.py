from django.shortcuts import render
from .models import Proizvod  
from django.shortcuts import render, get_object_or_404 



def index(request):
    return render(request, 'shop/index.html')

def katalog(request):
    kategorija_slug = request.GET.get('kategorija')
    sort_opcija = request.GET.get('sort') # Uzimamo parametar za sortiranje

    if kategorija_slug:
        proizvodi_iz_baze = Proizvod.objects.filter(kategorija=kategorija_slug)
    else:
        proizvodi_iz_baze = Proizvod.objects.all()
    if sort_opcija == 'cijena_asc':
        proizvodi_iz_baze = proizvodi_iz_baze.order_by('cijena')
    elif sort_opcija == 'cijena_desc':
        proizvodi_iz_baze = proizvodi_iz_baze.order_by('-cijena')

    return render(request, 'shop/katalog.html', {
        'proizvodi': proizvodi_iz_baze,
        'trenutna_kategorija': kategorija_slug # Šaljemo kategoriju da je ne izgubimo kod sortiranja
    })

def detalji_proizvoda(request, id):
    proizvod = get_object_or_404(Proizvod, id=id)
    return render(request, 'shop/detalji.html', {'proizvod': proizvod})


def kontakt(request):
    return render(request, 'shop/kontakt.html')