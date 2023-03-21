from django.contrib import admin
from store.models import ItemModel, CompanyModel, VehicleModel

# Register your models here.
admin.site.register(CompanyModel)
admin.site.register(VehicleModel)
admin.site.register(ItemModel)
