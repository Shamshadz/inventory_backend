from django.db import models

# Create your models here.


class CompanyModel(models.Model):
    company_name = models.CharField(max_length=1024)

    def __str__(self):
        return self.company_name


class ItemModel(models.Model):
    company_name = models.ForeignKey(
        CompanyModel, related_name='company', on_delete=models.CASCADE)
    vehicle_name = models.CharField(max_length=1024, blank=False)
    item_code = models.CharField(max_length=1024, blank=False)
    description = models.CharField(max_length=1024, blank=False)
    location = models.CharField(max_length=1024, blank=False)
    quantity = models.PositiveIntegerField(default=0)
    MRP = models.CharField(max_length=1024, blank=False)
    discount = models.CharField(max_length=1024)
    mech_selling_pr = models.CharField(max_length=1024)
    cust_selling_pr = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_code
