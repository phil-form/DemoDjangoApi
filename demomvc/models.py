from django.db import models

# Create your models here.
import datetime
from django.db import models

class BaseEntity(models.Model):
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    deletedat = models.DateTimeField(null=True, blank=True)
    active = models.BooleanField(default=True, name='active')
        
    class Meta:
        abstract = True
