from constant.models import Constant
from django.contrib import admin

class ContentAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Stałe',           	 {'fields': ['min_ilosc_oddanych','min_ilosc_zaakceptowanych','ilosc_wys_kacik_babuni']}),
        ('Email potwierdzający', {'fields': ['register_email_message']}),
    ]	

admin.site.register(Constant, ContentAdmin)