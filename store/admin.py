from django.contrib import admin
from store.models import (ItemModel, VCompanyModel, LocationModel,
                          DashBoardModel, CompanyModel, VehicleModel, DelayTranscation)

# Register your models here.
admin.site.register(VCompanyModel)
admin.site.register(CompanyModel)
admin.site.register(VehicleModel)
admin.site.register(ItemModel)
admin.site.register(DashBoardModel)
admin.site.register(LocationModel)
admin.site.register(DelayTranscation)

## Medical Register Models
from store.models import (MedicineModel, MedLocationModel, MedDashBoardModel, MedicineCategoryModel)

admin.site.register(MedicineCategoryModel)
admin.site.register(MedicineModel)
admin.site.register(MedLocationModel)
admin.site.register(MedDashBoardModel)