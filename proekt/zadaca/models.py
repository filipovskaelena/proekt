from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Kategorija(models.Model):
    ime = models.CharField(max_length=50)
    opis = models.CharField(max_length=100)
    aktivna = models.CharField(max_length=2)

class Korisnik(models.Model):
    django_user = models.ForeignKey(User, on_delete=models.CASCADE)

class Produkt(models.Model):
    sifra = models.CharField(max_length=30)
    ime = models.CharField(max_length=50)
    opis = models.CharField(max_length=50)
    kategorija = models.ForeignKey(Kategorija, on_delete=models.CASCADE)
    korisnik = models.ForeignKey(Korisnik, on_delete=models.CASCADE)
    cena = models.IntegerField()
    kolicina = models.IntegerField()

class Klient(models.Model):
    ime = models.CharField(max_length=50)
    prezime = models.CharField(max_length=50)
    adresa = models.CharField(max_length=50)
    email = models.CharField(max_length=50)


class Prodazba(models.Model):
    produkt = models.ForeignKey(Produkt, on_delete=models.CASCADE)
    datum = models.DateField()
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)


