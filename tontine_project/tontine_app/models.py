from django.db import models
from django.contrib.auth.models import User

class Cotisation(models.Model):
    utilisateur = models.ForeignKey(User, related_name='cotisations_tontine_app', on_delete=models.CASCADE)
    # Autres champs de modèle

    # Ajoutez d'autres champs pour les informations personnelles et l'historique des transactions

class GroupeTontine(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    montant_cotisation = models.CharField(max_length=100)
    frequence_paiements = models.CharField(max_length=50)

    def __str__(self):
	    return  self.nom
    # Ajoutez d'autres champs selon vos besoins

class Membre(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    groupe_tontine = models.ForeignKey(GroupeTontine, on_delete=models.CASCADE)
    
    

class Paiement(models.Model):
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type_paiement = models.CharField(max_length=50, null=True)  # Par exemple : cotisation, autres
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    groupe_tontine = models.ForeignKey(GroupeTontine, on_delete=models.CASCADE)

class Contact(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150) 
    telephone = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, null=True, blank=True)  

    def __str__(self):
	    return  f"{self.prenom} {self.nom}"  
    
class Role(models.Model):
    nom = models.CharField(max_length=150)  
          
    
   
    
