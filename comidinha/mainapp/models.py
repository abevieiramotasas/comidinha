from django.contrib.gis.db import models

class DonorHouse(models.Model):
    # TODO como descrever endereco fisico? utilizando um ponto
    address = models.PointField()
    # TODO como descrever telefone?
    # > mesmo em models.Donor.phone
    # > mesmo em models.Distributor.phone
    # > mesmo em models.DistributionCenter.phone
    phone = models.CharField(max_length=12)
    login = models.CharField(max_length=12, unique=True)
    # TODO como tratar password?
    password = models.CharField(max_length=12)
    public = models.BooleanField()
    # TODO ver como funciona
    # TODO unique para um field funciona por tabela, o que nao eh a intencao aqui
    #      ou retira o homepage como unico, ou o coloca numa tabela, ou faz a verificacao correta
    homepage = models.URLField(unique=True)
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
        
class Distributor(models.Model):
    description = models.TextField()
    homepage = models.URLField(unique=True)
    phone = models.CharField(max_length=12)
    # TODO melhor usar PointField ou (lat, lon) ?
    position = models.PointField()
    # TODO como descrever capacidade?
    height = models.IntegerField()
    volume = models.IntegerField()
    
    def __unicode__(self):
        return self.homepage
        
        
class DistributionCenter(models.Model):
    description = models.TextField()
    homepage = models.URLField(unique=True)
    phone = models.CharField(max_length=12)
    # TODO como descrever a necessidade de alimentos?!
    necessity = models.IntegerField()
    
    def __unicode__(self):
        return self.description
        
        
class Food(models.Model):
    description = models.TextField()
    donor_house = models.ForeignKey(DonorHouse)
    # TODO como utilizar unidades de medida diversas?
    # > mesmo para volume
    height = models.IntegerField()
    volume = models.IntegerField()
    distributor = models.ForeignKey(Distributor, blank=True)
    distribution_center = models.ForeignKey(DistributionCenter, blank=True)
    STATUS_OF_DELIVERY = (
        ('0', 'In donor'), 
        ('1', 'Distributor allocated'),
        ('2', 'With distributor'),
        ('3', 'In distribution center'),
        ('4', 'Delivered'),    
    )
    status = models.CharField(max_length=1, choices=STATUS_OF_DELIVERY)
    # TODO este campo deve representar periodos nos quais o distributor pode coletar o alimento    
    availability = models.DateTimeField()
    
    def __unicode__(self):
        return self.description
    
