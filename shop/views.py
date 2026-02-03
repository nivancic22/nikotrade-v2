from django.shortcuts import render

def index(request):
    return render(request, 'shop/index.html')

def katalog(request):
    #dohvatanje proizvoda iz baze
    return render(request, 'shop/katalog.html')

def kontakt(request):
    return render(request, 'shop/kontakt.html')