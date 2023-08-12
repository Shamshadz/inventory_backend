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
    quantity_limit = models.IntegerField(default=2)
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
    item_code = models.CharField(max_length=1024,blank=True,null=True)
    description = models.CharField(max_length=1024,null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=1)
    sold_to = models.CharField(max_length=1024,null=True,blank=True)
    sold_at = models.CharField(max_length=1024,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_code
    
class DelayTranscation(models.Model):
    name = models.CharField(max_length=1024,blank=True)
    description = models.CharField(max_length=1023,blank=True)
    amount = models.IntegerField(null=False, blank=True)
    deadline = models.DateField(null=True, blank=True)
    is_pending = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.amount) + "  " + self.name


#### Medical Model
class MedicineCategoryModel(models.Model):
    category = models.CharField('medicine_category', max_length=1024)

    def __str__(self):
        return self.category

class MedicineModel(models.Model):
    category = models.ForeignKey(MedicineCategoryModel, on_delete=models.CASCADE)
    name = models.CharField('Medicine Name', max_length=1024)
    manufacturer = models.CharField("Manufacturer", max_length=1024)
    description = models.TextField("Description or Ingredient", max_length=1024)
    price = models.PositiveIntegerField("Medicine Price")
    customer_price = models.PositiveIntegerField("Customer Selling Price",null=True)
    quantity = models.PositiveBigIntegerField("Quantity")
    quantity_limit = models.IntegerField(default=2)
    location = models.CharField("Rack Location Medicine", max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name
    
class MedLocationModel(models.Model):
    photo = models.ImageField(blank=True,null=True)
    location = models.CharField(max_length=1024)

    def __str__(self):
        return self.location
    
class MedDashBoardModel(models.Model):
    category = models.CharField(max_length=1024,blank=True,null=True)
    name = models.CharField(max_length=1024,blank=True,null=True)
    description = models.CharField(max_length=1024,null=True, blank=True)
    quantity = models.PositiveBigIntegerField(default=1)
    sold_at = models.CharField(max_length=1024,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name