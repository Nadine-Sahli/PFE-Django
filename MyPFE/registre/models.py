from django.db import models
from django.contrib.gis.db import models




class composteur(models.Model):
    nom=models.CharField(max_length=100,null=True)
    prenom=models.CharField(max_length=100,null=True)
    NB_GSM=models.CharField(max_length=100,null=True)
    pseudo=models.CharField(max_length=100,null=True)
    e_mail=models.EmailField(max_length=100,null=True)
    
    

    composteur_id=models.CharField(max_length=100,null=True, unique=True)
    # client = models.ForeignKey(client, on_delete=models.CASCADE, null=True, related_name='%(class)s_related')

    # image=models.ImageField(null=True)
    

    def __str__(self):
        return f"{self.prenom} {self.nom}"
    

class client(models.Model):
    nom=models.CharField(max_length=100,null=True)
    prenom=models.CharField(max_length=100,null=True)
    NB_GSM=models.CharField(max_length=100,null=True)
    pseudo=models.CharField(max_length=100,null=True)
    e_mail=models.EmailField(max_length=100,null=True)
    # image=models.ImageField(null=True)

    client_id=models.CharField(max_length=100,null=True, unique=True)

    composteur = models.ForeignKey(composteur, on_delete=models.CASCADE, null=True, related_name='%(class)s_related')

    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    #position=models.PointField(null=True)
    # image=models.ImageField(null=True)
    def __str__(self):
        return f"{self.prenom} {self.nom}"

# Create your models here.
