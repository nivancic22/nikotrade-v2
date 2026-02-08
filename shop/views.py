from django.shortcuts import render, redirect, get_object_or_404
from .models import Proizvod, Upit, KontaktUpit
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage  # Koristimo ovo za napredno slanje (Reply-To)

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

def politika_privatnosti(request):
    return render(request, 'shop/politika_privatnosti.html')

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
        # 2. Pripremi mail s Reply-To funkcijom
        subject = f"🛒 Upit za {proizvod.naziv} od: {email_kupca}"
        full_message = f"""
        Novi upit za proizvod: {proizvod.naziv}
        ------------------------------------------
        👤 Kupac: {email_kupca}
        
        💬 Poruka:
        {poruka}
        ------------------------------------------
        """
        
        try:
            email = EmailMessage(
                subject=subject,
                body=full_message,
                from_email=settings.EMAIL_HOST_USER, # Šalje server
                to=[settings.CONTACT_EMAIL],         # Primaš ti
                reply_to=[email_kupca]               # <--- Odgovor ide kupcu!
            )
            email.send(fail_silently=False)
            
            messages.success(request, "Upit je uspješno poslan!")
        except Exception as e:
            messages.error(request, "Došlo je do greške pri slanju maila.")
            print(f"Greška maila: {e}")

        return redirect('detalji', id=proizvod.id)

def posalji_kontakt_upit(request):
    if request.method == 'POST':
        email_posiljatelja = request.POST.get('email')
        naslov_poruke = request.POST.get('naslov')
        sadrzaj = request.POST.get('poruka')
        
        try:
            # 1. Spremi u bazu
            novi_kontakt = KontaktUpit(
                email=email_posiljatelja,
                naslov=naslov_poruke,
                poruka=sadrzaj
            )
            novi_kontakt.save() 
            
            # 2. Pripremi mail s Reply-To funkcijom
            subject_maila = f"📩 Kontakt: {naslov_poruke} (od {email_posiljatelja})"
            
            full_message = f"""
            Dobili ste novi upit jednog od naših posjetitelja!
            ------------------------------------------
            👤 Šalje: {email_posiljatelja}
            📝 Naslov: {naslov_poruke}
            
            💬 Poruka:
            {sadrzaj}
            ------------------------------------------
            *Kliknite 'Odgovori' (Reply) za direktan odgovor korisniku.
            """
            
            email = EmailMessage(
                subject=subject_maila,
                body=full_message,
                from_email=settings.EMAIL_HOST_USER,
                to=[settings.CONTACT_EMAIL],
                reply_to=[email_posiljatelja]        # <--- Odgovor ide pošiljatelju!
            )
            email.send(fail_silently=False)
            
            messages.success(request, "Vaša poruka je uspješno poslana! Javit ćemo vam se uskoro.")
            
        except Exception as e:
            messages.error(request, "Došlo je do greške. Molimo pokušajte ponovno.")
            print(f"Greška: {e}")

    return redirect('kontakt')