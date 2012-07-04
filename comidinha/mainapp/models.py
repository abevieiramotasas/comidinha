from django.contrib.gis.db import models

# common fields
# campo de telefone
# TODO validator
class PhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        super(PhoneField, self).__init__(*args, **kwargs)
        
        
class HomepageField(models.URLField):
    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        kwargs['null'] = True
        super(HomepageField, self).__init__(*args, **kwargs)
        

class DonorHouse(models.Model):
    # TODO como descrever endereco fisico? utilizando um ponto
    address = models.PointField()
    # TODO como descrever telefone?
    phone = PhoneField()
    login = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=12)
    homepage = HomepageField()
    # TODO limitar tamanho?
    description = models.TextField()
    
    def __unicode__(self):
        return self.login


class Donor(models.Model):
    name = models.CharField(max_length=30)
    phone = PhoneField()
    house = models.ForeignKey(DonorHouse)
    
    def __unicode__(self):
        return self.name
        
        
class Distributor(models.Model):
    description = models.TextField()
    homepage = HomepageField()
    phone = PhoneField()
    # TODO melhor usar PointField ou (lat, lon) ?
    position = models.PointField()
    # TODO como descrever capacidade?
    height = models.IntegerField()
    volume = models.IntegerField()
    
    def __unicode__(self):
        return self.homepage
        
        
class DistributionCenter(models.Model):
    description = models.TextField()
    homepage = models.URLField(blank=True, null=True)
    phone = PhoneField()
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
    distributor = models.ForeignKey(Distributor, blank=True, null=True)
    distribution_center = models.ForeignKey(DistributionCenter, blank=True, null=True)
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
    
