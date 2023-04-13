from django.contrib import admin
from django.contrib.gis import admin
from .models import *


# Register your models here.

# admin.site.register(nodes)




class nodesAdmin(admin.OSMGeoAdmin):
    list_display = ('Name', 'Position')
    search_fields = ('Name',)
    list_filter = ('Name',)

admin.site.register(nodes, nodesAdmin)




