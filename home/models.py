# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Rekeningcategorie(models.Model):

    #__Rekeningcategorie_FIELDS__
    naam = models.CharField(max_length=255, null=True, blank=True)
    beschrijving = models.TextField(max_length=255, null=True, blank=True)
    kleur = models.CharField(max_length=255, null=True, blank=True)
    icoon = models.CharField(max_length=255, null=True, blank=True)
    volgorde = models.IntegerField(null=True, blank=True)

    #__Rekeningcategorie_FIELDS__END

    class Meta:
        verbose_name        = _("Rekeningcategorie")
        verbose_name_plural = _("Rekeningcategorie")


class Rekening(models.Model):

    #__Rekening_FIELDS__
    type = models.CharField(max_length=255, null=True, blank=True)
    categorie = models.ForeignKey(RekeningCategorie, on_delete=models.CASCADE)
    banknaam = models.CharField(max_length=255, null=True, blank=True)
    rekeningnummer = models.CharField(max_length=255, null=True, blank=True)
    iban = models.CharField(max_length=255, null=True, blank=True)
    huidig_saldo = models.CharField(max_length=255, null=True, blank=True)
    begin_saldo = models.CharField(max_length=255, null=True, blank=True)
    kredietlimiet = models.CharField(max_length=255, null=True, blank=True)
    rente_percentage = models.CharField(max_length=255, null=True, blank=True)
    minimum_saldo_waarschuwing = models.CharField(max_length=255, null=True, blank=True)
    kleur = models.CharField(max_length=255, null=True, blank=True)
    icoon = models.CharField(max_length=255, null=True, blank=True)
    volgorde = models.IntegerField(null=True, blank=True)
    valuta = models.CharField(max_length=255, null=True, blank=True)
    notificaties_ingeschakeld = models.BooleanField()
    laatste_synchronisatie = models.DateTimeField(blank=True, null=True, default=timezone.now)
    externe_rekening_id = models.CharField(max_length=255, null=True, blank=True)
    notities = models.TextField(max_length=255, null=True, blank=True)

    #__Rekening_FIELDS__END

    class Meta:
        verbose_name        = _("Rekening")
        verbose_name_plural = _("Rekening")



#__MODELS__END
