from django.contrib import admin
from .models import Month, Customer, Slokketype, Extinguishant, Objekt
from import_export.admin import ImportExportModelAdmin

class MonthAdmin(ImportExportModelAdmin):
    pass

class CustomerAdmin(ImportExportModelAdmin):
    pass

class SlokketypeAdmin(ImportExportModelAdmin):
    pass

class ExtinguishantAdmin(ImportExportModelAdmin):
    pass

class ObjektAdmin(ImportExportModelAdmin):
    pass

# Register your models here.
admin.site.register(Month, MonthAdmin),
admin.site.register(Customer, CustomerAdmin),
admin.site.register(Slokketype, SlokketypeAdmin),
admin.site.register(Extinguishant, ExtinguishantAdmin),
admin.site.register(Objekt, ObjektAdmin),
