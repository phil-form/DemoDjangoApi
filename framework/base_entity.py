import datetime
from django.db import models

class BaseEntity:
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    deletedat = models.DateTimeField(null=True, blank=True)
    __active = models.BooleanField(default=True, name='active')
    
    @property
    def active(self):
        return self.__active

    @active.setter
    def active(self, value):
        if not value:
            self.deletedat = datetime.datetime.now()
        self.__active = value
