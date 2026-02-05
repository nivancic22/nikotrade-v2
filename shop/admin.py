from django.contrib import admin
from .models import Proizvod, DodatnaSlika # Provjeri jesu li oba ovdje

class DodatnaSlikaInline(admin.TabularInline):
    model = DodatnaSlika
    extra = 3

@admin.register(Proizvod)
class ProizvodAdmin(admin.ModelAdmin):
    # Koristimo 'naziv' jer smo vidjeli na slici da se tako zove polje
    list_display = ['naziv', 'cijena', 'kategorija'] 
    inlines = [DodatnaSlikaInline]