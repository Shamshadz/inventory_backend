from django.contrib import admin
from store.models import ItemModel, CompanyModel

# Register your models here.
admin.site.register(CompanyModel)
admin.site.register(ItemModel)
