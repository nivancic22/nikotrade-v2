from django.contrib import admin
from .models import Proizvod, DodatnaSlika # Provjeri jesu li oba ovdje
from .models import Upit


class DodatnaSlikaInline(admin.TabularInline):
    model = DodatnaSlika
    extra = 3

@admin.register(Proizvod)
class ProizvodAdmin(admin.ModelAdmin):
    # Koristimo 'naziv' jer smo vidjeli na slici da se tako zove polje
    list_display = ['naziv', 'cijena', 'kategorija'] 
    inlines = [DodatnaSlikaInline]


@admin.register(Upit)
class UpitAdmin(admin.ModelAdmin):
    list_display = ['email_kupca', 'proizvod', 'datum_slanja']
    readonly_fields = ['datum_slanja']