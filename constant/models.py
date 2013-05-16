from django.db import models

class Constant(models.Model):
	min_ilosc_oddanych = models.IntegerField(default=10)
	min_ilosc_zaakceptowanych = models.IntegerField(default =20)
	ilosc_wys_kacik_babuni = models.IntegerField(default =3)
	register_email_message = models.TextField("{{link}}")