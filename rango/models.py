from django.db import models

# Create your models here.
#CATEGORY
class Bares(models.Model):
    name = models.CharField(max_length=128, unique=True)
    direccion = models.CharField(max_length=200)
    visitas = models.IntegerField(default=0)
    
    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.name

    def votar(self):
        self.n_visita +=1

#PAGE
class Tapas(models.Model):
    barname = models.ForeignKey(Bares) #category
    name = models.CharField(max_length=120, unique=True)
    votos = models.IntegerField(default=0)

    def __unicode__(self):      #For Python 2, use __str__ on Python 3
        return self.name