from django.db import models
from django.contrib.auth.models import User

class User_data(models.Model):
	random_activate_code = models.IntegerField(default =3)
	user = models.OneToOneField(User, primary_key=True)