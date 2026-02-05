from django.db import models

class Proizvod(models.Model):
    KATEGORIJE = (
        ('miris', 'Automiris - Dres'),
        ('oprema', 'Sportska Oprema'),
        ('case', 'Gravirane čaše'), 
    )

    naziv = models.CharField(max_length=200)
    kategorija = models.CharField(max_length=20, choices=KATEGORIJE)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    # Slika se sprema u mapu 'proizvodi' unutar tvojih medijskih datoteka
    slika = models.ImageField(upload_to='proizvodi/', blank=True, null=True)
    datum_dodavanja = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.naziv
    
class DodatnaSlika(models.Model):
    proizvod = models.ForeignKey('Proizvod', related_name='dodatne_slike', on_delete=models.CASCADE)
    slika = models.ImageField(upload_to='proizvodi/galerija/')

    def __str__(self):
        return f"Slika za {self.proizvod.naziv}"