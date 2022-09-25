from django.db import models
import hashlib
import os


def get_image_path(instance, filename):
    hashname = hashlib.sha1(filename.encode()).hexdigest() + '.jpg'
    return os.path.join('media', 'img', hashname[:2], hashname[2:4], hashname[4:6], hashname)

class backImg(models.Model):
    img = models.ImageField('Img', upload_to=get_image_path, default='none')
    name = models.CharField(max_length=200, default='none')

    def __str__(self):
        return f"{self.id}. {self.name}"

