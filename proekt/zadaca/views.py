from django.shortcuts import render, redirect
from .models import Produkt
from .form import ProduktForm

# Create your views here.
def index(request):
    return render(request, "index.html")

def outofstock(request):
    if request.method == 'POST':
        forma = ProduktForm(request.POST)
        if forma.is_valid():
            produkt = forma.save(commit=False)
            produkt.korisnik.django_user = request.user
            produkt.save()
            return redirect("outofstock.html")
    produkti = Produkt.objects.all()
    context = {'produkti':produkti, 'form':ProduktForm}
    return render(request, "outofstock.html", context=context)