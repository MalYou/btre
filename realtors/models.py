from django.db import models

from datetime import datetime

class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    description = models.TextField(blank=True)
    email = models.EmailField(max_length=50, unique=True, blank=False)
    phone = models.CharField( max_length=20, blank=True)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self) -> str:
        return self.name
