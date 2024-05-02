from django.contrib import admin
from .models import Cotisation

class CotisationAdmin(admin.ModelAdmin):
    list_display="firstname","lastname","country", "montant"

admin.site.register(Cotisation,CotisationAdmin)
