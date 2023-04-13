from django.db import models
from django.contrib.gis.db import models 
from django.contrib.gis.admin import OSMGeoAdmin


class nodes(models.Model):
    Name = models.CharField(max_length=50,blank=True, null=True)
    Position=models.PointField(null=True)
    Latitude =models.CharField(max_length=50, null=True , blank=True)
    Longitude =models.CharField(max_length=50, null=True,blank=True)
    
    def __str__(self):
        return "Node " + str(self.id) 
    
    class Meta:
       verbose_name_plural = "Nodes"
       verbose_name = "Node"


class nodesAdmin(OSMGeoAdmin):
    list_display = ('Name', 'Latitude', 'Longitude')
    search_fields = ('Name',)
    list_filter = ('Name',)





    






   
    

   




   

