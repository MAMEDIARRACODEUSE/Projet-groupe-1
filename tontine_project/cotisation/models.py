from django.db import models

class Cotisation(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    country=models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)  # Champ montant avec contrainte NOT NULL

    def __str__(self):
        return f"{self.firstname} {self.lastname} - {self.country}"