from django.db import models
from django.utils import timezone
# Create your models here.


class Month(models.Model):
    navn = models.CharField(max_length=100, default=None)
    
    def __str__(self):
        return self.navn

class Customer(models.Model):
    kunde = models.CharField(max_length=255)
    kundeinformasjon = models.CharField(max_length=255, null=True, blank=True)
    badresse = models.CharField(max_length=255, null=True, blank=True)
    bpostnr = models.PositiveSmallIntegerField(null=True, blank=True)
    bpoststed = models.CharField(max_length=255, null=True, blank=True)
    fadresse = models.CharField(max_length=255, null=True, blank=True)
    fpostnr = models.PositiveSmallIntegerField(null=True, blank=True)
    fpoststed = models.CharField(max_length=255, null=True, blank=True)
    kontaktperson = models.CharField(max_length=255, null=True, blank=True)
    tlf1 = models.PositiveIntegerField(null=True, blank=True)
    tlf2 = models.PositiveIntegerField(null=True, blank=True)
    nummer = models.PositiveIntegerField(null=True, blank=True)
    tripletex = models.PositiveIntegerField(null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    gml_id = models.TextField(null=True, blank=True)
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    aktiv = models.BooleanField(default=True)
    created = models.DateTimeField(editable=False)
    modified = models.DateTimeField()

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(Customer, self).save(*args, **kwargs)

    def __str__(self):
        return self.kunde + ' | ' + self.badresse + ' | ' + self.bpoststed