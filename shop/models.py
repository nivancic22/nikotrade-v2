from django.db import models

class Proizvod(models.Model):
    naziv = models.CharField(max_length=200)
    opis = models.TextField()
    cijena = models.DecimalField(max_digits=10, decimal_places=2)
    slika = models.ImageField(upload_to='proizvodi/')
    dostupno = models.BooleanField(default=True)

    def __str__(self):
        return self.naziv