from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Contact
from .models import GroupeTontine
from .models import Membre
from .models import Cotisation
from .models import Paiement





def home(request):
    return render(request, "pages/base.html")

def about(request):
    return render(request, "pages/about.html")

@login_required(login_url="/login/")
def groupe_list(request):
    groupes = GroupeTontine.objects.all()
    return render(request, "groupes/groupe_list.html", {"groupes": groupes})

@login_required(login_url="/login/")
def groupe_detail(request, id):
    groupeTontine = get_object_or_404(GroupeTontine, id=id)
    return render(request, "groupes/groupe_detail.html", {"groupeTontine": groupeTontine})
    

@login_required(login_url="/login/")
def liste_member(request):
    membre = Membre.objects.all()
    return render(request, "membres/liste_member.html", {"membres": membre})

@login_required(login_url="/login/")
def paiement(request):
    paiement = Paiement.objects.all()
    return render(request, "pages/paiement.html", {"paiement": paiement})

@login_required(login_url="/login/")
def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, "contacts/contact_list.html", {"contacts": contacts})

@login_required(login_url="/login/")
def contact_details(request, id):
    contact = get_object_or_404(Contact, id=id)
    return render(request, "contacts/contact_details.html", {"contact": contact})

@login_required(login_url="/login/")
def cotisation(request):
    cotisation = Cotisation.objects.all()
    return render(request, "cotisation/cotisation.html", {"cotisation": cotisation})


def index(request):
    mem=Cotisation.objects.all()
    return render(request,'cotisation.html',{'mem':mem})

def add(request):
    return render(request,'add.html')

def addrec(request):
    x=request.POST['montant']
    y=request.POST['last']
    z=request.POST['country']
    mem=Cotisation(montant=x,lastname=y,country=z)
    mem.save()
    return redirect("/")

def delete(request,id):
    mem=Cotisation.objects.get(id=id)
    mem.delete()
    return redirect("/")

def update(request,id):
    mem=Cotisation.objects.get(id=id)
    return render(request,'update.html',{'mem':mem})

def uprec(request,id):
    x=request.POST['montant']
    y=request.POST['last']
    z=request.POST['country']
    mem=Cotisation.objects.get(id=id)
    mem.montant=x
    mem.lastname=y
    mem.country=z
    mem.save()
    return redirect("/")

