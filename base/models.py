from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tache(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    titre = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    terminer= models.BooleanField(default=False)
    creer = models.DateTimeField(auto_now_add=True)

   
def __str__(self):
    return self.titre
   
class meta:
    ordering=['terminer']
        

