from django.shortcuts import render
from .models import Proizvod, Upit  
from django.shortcuts import render, redirect, get_object_or_404 
from django.core.mail import send_mail
from django.contrib import messages


def index(request):
    return render(request, 'shop/index.html')

def katalog(request):
    kategorija_slug = request.GET.get('kategorija')
    sort_opcija = request.GET.get('sort') 

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
        'trenutna_kategorija': kategorija_slug 
    })

def detalji_proizvoda(request, id):
    proizvod = get_object_or_404(Proizvod, id=id)
    return render(request, 'shop/detalji.html', {'proizvod': proizvod})


def kontakt(request):
    return render(request, 'shop/kontakt.html')



def posalji_upit(request, proizvod_id):
    if request.method == 'POST':
        proizvod = get_object_or_404(Proizvod, id=proizvod_id)
        email_kupca = request.POST.get('email_kupca')
        poruka = request.POST.get('poruka')

        # 1. Spremi u bazu
        Upit.objects.create(
            proizvod=proizvod,
            email_kupca=email_kupca,
            poruka=poruka
        )

        # 2. Pošalji mail tebi
        subject = f"Novi upit za: {proizvod.naziv}"
        full_message = f"Dobili ste novi upit za proizvod {proizvod.naziv}.\n\nEmail kupca: {email_kupca}\nPoruka:\n{poruka}"
        
        try:
            send_mail(
                subject,
                full_message,
                'nikoivancic2801@gmail.com', # Od koga (tvoj settings.EMAIL_HOST_USER)
                ['nikoivancic2801@gmail.com'], # Kome (tvoj testni mail)
                fail_silently=False,
            )
            messages.success(request, "Upit je uspješno poslan!")
        except Exception as e:
            messages.error(request, "Došlo je do greške pri slanju maila.")

        return redirect('detalji', id=proizvod.id)