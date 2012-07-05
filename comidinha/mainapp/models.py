from django.contrib.gis.db import models
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
# common fields
# campo de telefone
phone_re = re.compile(r'^\(([0-9]){2}\)-([0-9]){4}-([0-9]){4}$')
def validate_phone(phone):
    if not phone_re.match(phone):
        raise ValidationError(u'%s is not a valid phone number' % phone)
    
class PhoneField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 20
        kwargs['blank'] = False
        kwargs['null'] = False
        if 'validators' in kwargs:
            kwargs['validators'].append(validate_phone)
        else:
            kwargs['validators'] = [validate_phone]
        super(PhoneField, self).__init__(*args, **kwargs)
        

# campo de homepage                
class HomepageField(models.URLField):
    def __init__(self, *args, **kwargs):
        kwargs['blank'] = True
        kwargs['null'] = True
        super(HomepageField, self).__init__(*args, **kwargs)
        

# modelos
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)
    # outros atributos
    # TODO usando blank e null = True temporariamente
    # enquanto ainda nao vi o comportamento do PointField
    address = models.PointField(blank=True, null=True)
    phone = PhoneField()
    homepage = HomepageField()
    description = models.TextField()
    geo_objects = models.GeoManager()
    
    def __unicode__(self):
        return self.user.username
    
class DonorHouse(UserProfile):
    pass


class Donor(models.Model):
    name = models.CharField(max_length=30)
    phone = PhoneField()
    house = models.ForeignKey(DonorHouse)
    
    def __unicode__(self):
        return self.name
        
        
class Distributor(UserProfile):
    position = models.PointField()
    # TODO como descrever capacidade?
    # capacidade maxima
    max_height = models.IntegerField()
    max_volume = models.IntegerField()
    # capacidade utilizada
    height = models.IntegerField(default=0)
        
        
class DistributionCenter(UserProfile):
    # TODO como descrever a necessidade de alimentos?!
    necessity = models.IntegerField()
        
        
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
    
