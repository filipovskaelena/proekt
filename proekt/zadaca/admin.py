from django.contrib import admin
from .models import Produkt, Prodazba, Klient, Korisnik, Kategorija

# Register your models here.
class ProduktAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if obj:
            if request.user==obj.korisnik.django_user:
                return True
            return False

admin.site.register(Produkt, ProduktAdmin)

class ProdazbaAdmin(admin.ModelAdmin):
    pass

admin.site.register(Prodazba, ProdazbaAdmin)

class KlientAdmin(admin.ModelAdmin):
    list_display = ("ime", "prezime")

admin.site.register(Klient, KlientAdmin)

class KorisnikAdmin(admin.ModelAdmin):
    pass

admin.site.register(Korisnik, KorisnikAdmin)

class KategorijaAdmin(admin.ModelAdmin):
    list_display = ("ime",)
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        return False

admin.site.register(Kategorija, KategorijaAdmin)
