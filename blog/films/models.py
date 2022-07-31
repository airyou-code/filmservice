from django.db import models

# Create your models here.from email.policy import default
from django.db import models
import hashlib
import os


def get_image_path(instance, filename):
    hashname = hashlib.sha1(filename.encode()).hexdigest() + '.jpg'
    return os.path.join('media', 'img', hashname[:2], hashname[2:4], hashname[4:6], hashname)

class Ganer(models.Model):
    name = models.CharField(max_length=60, default='none')
    def __str__(self):
        return f"{self.id}. {self.name}"

class Country(models.Model):
    name = models.CharField(max_length=50, default='none')
    def __str__(self):
        return f"{self.id}. {self.name}"

class Age(models.Model):
    name = models.CharField(max_length=40, default='none')
    def __str__(self):
        return f"{self.id}. {self.name}"

class Year(models.Model):
    name = models.CharField(max_length=10, default='none')
    def __str__(self):
        return f"{self.id}. {self.name}"


class Film(models.Model):
    name = models.CharField(max_length=200, default='none')
    angl_name = models.CharField(max_length=200, default='none')
    id_film = models.CharField(max_length=100, default='none')
    img = models.ImageField('Img', upload_to=get_image_path, default='none')#
    url_img = script = models.CharField(max_length=300, default='none')

    tg_genre = models.ManyToManyField(Ganer, default='none')
    tg_country = models.ManyToManyField(Country)
    tg_year = models.ManyToManyField(Year)
    tg_age = models.ManyToManyField(Age)

    yearProd = models.CharField(max_length=10, default='none')#
    country = models.CharField(max_length=40, default='none')#
    genre = models.CharField(max_length=200, default='none')
    director = models.CharField(max_length=100, default='none')
    script = models.CharField(max_length=300, default='none')
    producer = models.CharField(max_length=200, default='none')
    Operator = models.CharField(max_length=200, default='none')
    Budget = models.CharField(max_length=40, default='none')
    Fees = models.CharField(max_length=100, default='none')
    premiere = models.CharField(max_length=40, default='none')
    Age = models.CharField(max_length=40, default='none')#
    rating = models.CharField(max_length=40, default='none')
    time = models.CharField(max_length=40, default='none')

    description = models.TextField(default='none')
    dateTime = models.DateTimeField('dateTime', auto_now=True)

    def __str__(self):
        return f"{self.id}. {self.name}"





