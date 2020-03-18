from django.db import models
# Create your models here.


class Month(models.Model):
    navn = models.CharField(max_length=100, default=None)
    
    def __str__(self):
        return self.navn
