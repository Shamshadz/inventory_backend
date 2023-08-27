from django.contrib import admin
from store.models import (ItemModel, VCompanyModel, LocationModel,
                          DashBoardModel, CompanyModel, VehicleModel, DelayTranscation)

from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

# Register your models here.
User = get_user_model()

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            None,
            {"fields": ("profile_pic", "mobile", "name", "email")},
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("date_joined",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "profile_pic",
                    "mobile",
                    "name",
                    "email",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "user_permissions",
                ),
            },
        ),
    )
    list_display = [
        "id",
        "mobile",
        "name",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    list_display_links = [
        "id",
        "name",
        "mobile",
        "is_active",
        "is_staff",
        "is_superuser",
    ]
    list_filter = [
        "is_staff",
        "is_superuser",
        "is_active",
    ]
    search_fields = ["mobile", "name"]
    readonly_fields = ["last_login", "date_joined"]
    ordering = ["mobile"]
    exclude = ["username", "password"]

# Register your models here.
admin.site.register(VCompanyModel)
admin.site.register(CompanyModel)
admin.site.register(VehicleModel)
admin.site.register(ItemModel)
admin.site.register(DashBoardModel)
admin.site.register(LocationModel)
admin.site.register(DelayTranscation)

## Medical Register Models
from store.models import (MedicineModel, MedLocationModel, MedDashBoardModel,
                           MedicineCategoryModel)

admin.site.register(MedicineCategoryModel)
admin.site.register(MedicineModel)
admin.site.register(MedLocationModel)
admin.site.register(MedDashBoardModel)