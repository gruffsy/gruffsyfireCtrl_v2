from django.contrib import admin
from .models import Month, Customer, Extinguishant, Slokketype, Object, ObjTr, Avvik
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class AvvikAdmin(ImportExportModelAdmin):
    pass

class CustomerAdmin(ImportExportModelAdmin):
    pass


class ExtinguishantAdmin(ImportExportModelAdmin):
    pass


class ObjectAdmin(ImportExportModelAdmin):
    pass


class SlokketypeAdmin(ImportExportModelAdmin):
    pass


class ObjTrAdmin(ImportExportModelAdmin):
    pass


# Register your models here.

admin.site.register(Month),
admin.site.register(Customer, CustomerAdmin),
admin.site.register(Slokketype, SlokketypeAdmin),
admin.site.register(Extinguishant, ExtinguishantAdmin),
admin.site.register(Object, ObjectAdmin),
admin.site.register(ObjTr, ObjTrAdmin)
admin.site.register(Avvik, AvvikAdmin),

