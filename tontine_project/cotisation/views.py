from django.shortcuts import render, redirect
from .models import Cotisation

def add(request):
    return render(request, 'cotisation/add.html')

def addrec(request):
    if request.method == 'POST':
        x = request.POST.get('firstname')  # Récupérer la valeur du champ firstname depuis le formulaire
        y = request.POST.get('last')
        z = request.POST.get('country')
        m = request.POST.get('montant')
        if x:  # Vérifier si firstname n'est pas vide
            cotisation = Cotisation.objects.create(firstname=x, lastname=y, country=z, montant=m)
            return redirect("/")
        else:
            return render(request, 'cotisation/add.html', {'error_message': 'Le prénom est obligatoire.'})
    else:
        return redirect("/cotisation/")


def delete(request, id):
    cotisation = Cotisation.objects.get(pk=id)
    cotisation.delete()
    return redirect("/")

def update(request, id):
    cotisation = Cotisation.objects.get(pk=id)
    return render(request, 'update.html', {'cotisation': cotisation})

def uprec(request, id):
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('last')
        country = request.POST.get('country')
        montant = request.POST.get('montant')  # Correction: récupérer la valeur du champ montant
        cotisation = Cotisation.objects.get(pk=id)
        cotisation.firstname = firstname
        cotisation.lastname = lastname
        cotisation.country = country
        cotisation.montant = montant

        cotisation.save()
        return redirect("/cotisation/")
