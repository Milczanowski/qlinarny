from django.db import models
from django.contrib.auth.models import User


class Kategoria(models.Model):
	nazwa = models.CharField(max_length=255)

class Przepis(models.Model):
	user = models.ForeignKey(User);
	nazwa = models.CharField(max_length=255)
	data_ododania =  models.DateTimeField()
	data_losowania =  models.DateTimeField()
	zatwierdzony = models.BooleanField()
	potwiedzony = models.BooleanField()
	rating = models.IntegerField(default =3)
	czas_przygotowania = models.IntegerField()
	trudnosc = models.IntegerField(default = 5)
	ilosc_porcji = models.IntegerField(default =1)
	skladniki = models.TextField("")
	sposob_przygotowania = models.TextField("")
	uwagi = models.TextField("")
	kategoria = models.OneToOneField(Kategoria)




