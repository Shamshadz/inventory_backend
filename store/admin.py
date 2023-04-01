from django.contrib import admin
from store.models import (ItemModel, VCompanyModel, LocationModel,
                          DashBoardModel, CompanyModel, VehicleModel)

# Register your models here.
admin.site.register(VCompanyModel)
admin.site.register(CompanyModel)
admin.site.register(VehicleModel)
admin.site.register(ItemModel)
admin.site.register(DashBoardModel)
admin.site.register(LocationModel)