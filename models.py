from audioop import maxpp
from pickle import TRUE
from pyexpat import model
from tkinter import CASCADE
from unicodedata import name
from django.db import models
from django.forms import CharField

class FORMATEUR(models.Model):
     
      name_formateur = models.CharField( max_length=50)
      prenom_formateur= models.CharField(max_length=50)
      adress_formateur= models.CharField(max_length=50)
      age_formateur= models.IntegerField
      theme = models.ForeignKey("Theme", on_delete=models.SET_NULL, null=True, blank=True)

class THEME(models.Model):
    name_th = models.CharField(max_length=50)
    domane = models.ForeignKey("DOMAINE",on_delete=models.CASCADE)

class DOMAINE(models.Model):
    name_domaine= models.CharField(max_length=40) 

class CLIENT(models.Model):
   
    name_client=models.CharField(max_length=50)

class BENEFICIAIRE(models.Model):
    
    prenom_beneficiare= models.CharField(max_length=40)
    nom_beneficiare = models.CharField( max_length=50)
    adress_beneficiaire = models.CharField(max_length=50)
    age_beneficiaire =models.IntegerField
    client= models.ForeignKey("CLIENT", on_delete=models.CASCADE)

class formation(models.Model):
   formateur_formation=models.ForeignKey("FORMATEUR",on_delete=models.CASCADE)
   theme_formation=models.ForeignKey("THEME",on_delete=models.CASCADE)
   client=models.ForeignKey("CLIENT",on_delete=models.CASCADE)
   
