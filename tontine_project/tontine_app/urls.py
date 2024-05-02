from django.urls import path
from .views import home, about, groupe_list, groupe_detail, paiement,  liste_member, cotisation, contact_list, contact_details


urlpatterns = [
	path("", home, name="base"),
    path("about/", about, name="about"),
    path("groupes/", groupe_list, name="groupes"),
    path("groupes/<int:id>/", groupe_detail, name="detail"),
    path("paiement/", paiement, name="paiement"),
    path("membres/", liste_member, name="membres"),
    path("cotisation/", cotisation, name="cotisation"),
    path("contacts/", contact_list, name="contacts"),
    path("contacts/<int:id>/", contact_details, name="details"),
]