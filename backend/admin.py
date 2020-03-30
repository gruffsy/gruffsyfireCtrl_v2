from django.contrib import admin
from .models import Month, Customer, Extinguishant, Slokketype, Object, ObjTr, Avvik

# Register your models here.

admin.site.register(Month)
admin.site.register(Customer)
admin.site.register(Slokketype)
admin.site.register(Extinguishant)
admin.site.register(ObjTr)
admin.site.register(Object)
admin.site.register(Avvik)

