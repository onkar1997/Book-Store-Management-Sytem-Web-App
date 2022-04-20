from django.db import models
from stores.models import Store
from datetime import datetime


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    author_name = models.CharField(max_length=200)
    publisher_name = models.CharField(max_length=200)
    num_of_copies = models.IntegerField(default=0)
    price = models.IntegerField(null=True)
    book_image = models.ImageField(
        upload_to='pics/books', default='noimage.png')
    pub_date = models.DateTimeField(default=datetime.now, blank=True)
    store_id = models.IntegerField()

    def __str__(self):
        return self.book_name
