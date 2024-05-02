from django.contrib import admin
from .models import GroupeTontine
from .models import Membre
from .models import Cotisation
from .models import Paiement
from .models import Contact
from .models import Role



admin.site.register(GroupeTontine)
admin.site.register(Membre)
admin.site.register(Cotisation)
admin.site.register(Paiement)
admin.site.register(Contact)
admin.site.register(Role)






