from django.db import models

# Create your models here.


class CompanyModel(models.Model):
    company_name = models.CharField(max_length=1024, blank=False)

    def __str__(self):
        return self.company_name
        
class VCompanyModel(models.Model):
    vcompany_name = models.CharField(max_length=1024, blank=False)

    def __str__(self):
        return self.vcompany_name

class VehicleModel(models.Model):
    vcompany = models.ForeignKey(
        VCompanyModel, related_name='vCompany', on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=1024, blank=False)

    def __str__(self):
        return self.vehicle_name

class ItemModel(models.Model):
    company_name = models.ForeignKey(
        CompanyModel, related_name='company', on_delete=models.CASCADE)
    vehicle_name = models.ForeignKey(
        VehicleModel, related_name='vehicle', on_delete=models.CASCADE)
    item_code = models.CharField(max_length=1024, unique=True, blank=True)
    description = models.CharField(max_length=1024, blank=False)
    location = models.CharField(max_length=1024, blank=False)
    quantity = models.PositiveIntegerField(default=0)
    MRP = models.CharField(max_length=1024, blank=False)
    mech_selling_pr = models.CharField(max_length=1024)
    cust_selling_pr = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_code
    
class LocationModel(models.Model):
    photo = models.ImageField(blank=True,null=True)
    location = models.CharField(max_length=1024)

    def __str__(self):
        return self.location

class DashBoardModel(models.Model):
    item = models.ForeignKey(
        ItemModel, related_name='item', on_delete=models.CASCADE
    )
    sold_to = models.CharField(max_length=1024,null=True,blank=True)
    sold_at = models.CharField(max_length=1024,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item.item_code