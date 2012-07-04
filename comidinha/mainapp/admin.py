from django.contrib.gis import admin
from models import DonorHouse, Donor, Distributor, DistributionCenter, Food

# admin.site.register(DonorHouse, admin.GeoModelAdmin)

class DonorInline(admin.TabularInline):
    model = Donor
    extra = 1    
class DonorHouseAdmin(admin.OSMGeoAdmin):
    inlines = [DonorInline]
    
    
#class DonorHouseInline(admin.TabularInline):
#    model = DonorHouse
#    extra = 1
#class DistributorInline(admin.TabularInline):
#    model = Distributor
#    extra = 1
#class DistributionCenterInline(admin.TabularInline):    
#    model = DistributionCenter
#    extra =  1
class FoodAdmin(admin.OSMGeoAdmin):
#    inlines = [DonorHouseInline, DistributionCenterInline, DistributorInline]    
    pass        
admin.site.register(Food, FoodAdmin)
admin.site.register(Distributor, admin.OSMGeoAdmin)
admin.site.register(DistributionCenter, admin.OSMGeoAdmin)        
admin.site.register(DonorHouse, DonorHouseAdmin)
admin.site.register(Donor, admin.OSMGeoAdmin)
