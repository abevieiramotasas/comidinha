from django.contrib.gis.db import models

class DonorHouse(models.Model):
    # TODO como descrever endereco fisico? utilizando um ponto
    address = models.PointField()
    # TODO como descrever telefone?
    # > mesmo em models.Donor.phone
    phone = models.CharField(max_length=12)
    login = models.CharField(max_length=12)
    # TODO como tratar password?
    password = models.CharField(max_length=12)
    public = models.BooleanField()
    # TODO ver como funciona
    homepage = models.URLField()
    # TODO limitar tamanho?
    description = models.TextField()
    
    def __unicode__(self):
        return self.login


class Donor(models.Model):
    # TODO setar vocativos | qual traducao pro ingreis?
    vocativo = models.CharField(max_length=6)
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=12)
    house = models.ForeignKey(DonorHouse)
    
    def __unicode__(self):
        return self.name
