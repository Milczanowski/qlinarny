# _*_ coding: utf-8 _*_
from django import forms
from django.core.exceptions import ObjectDoesNotExist

class FormularzLogowania(forms.Form):    
    nazwa = models.CharField(label="Nazwa", max_length=255)  
    czas_przygotowania = models.IntegerField(label="Czas przygotowania (minuty)")
    trudnosc = models.IntegerField(label = "Trudność (od 1 do 9)")
    ilosc_porcji = models.IntegerField(label= "Ilość porcji")
    skladniki = models.TextField(Label= "Składniki")
    sposob_przygotowania = models.TextField(label="Sposób przygotowania")
    uwagi = models.TextField(Uabel = "Uwagi")
    kategoria = models.OneToOneField(Kategoria, Label="Kategoria")