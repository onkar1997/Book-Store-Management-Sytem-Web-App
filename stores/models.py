from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Store(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    store_name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=200)
    address = models.TextField(null=True)
    store_image = models.ImageField(
        upload_to='pics/stores', default='noimage.png')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.store_name
