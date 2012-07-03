from django.contrib.gis import admin
from models import DonorHouse, Donor

# admin.site.register(DonorHouse, admin.GeoModelAdmin)

class ChoiceInline(admin.TabularInline):
    model = Donor
    extra = 2
    
class DonorHouseAdmin(admin.OSMGeoAdmin):
    inlines = [ChoiceInline]
    
        
admin.site.register(DonorHouse, DonorHouseAdmin)
admin.site.register(Donor, admin.OSMGeoAdmin)
