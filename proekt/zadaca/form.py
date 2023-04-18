from .models import Produkt
from django import forms

class ProduktForm(forms.ModelForm):
    class Meta:
        model = Produkt
        exclude = ("korisnik",)