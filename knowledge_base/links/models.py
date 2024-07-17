# from django.conf.global_settings import AUTH_USER_MODEL
# from django.contrib.auth.models import AbstractUser
from django.db import models
from django_jsonform.models.fields import JSONField
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.translation import gettext_lazy as _


# Create your models here.
from links.CustomUser import AbstractUser


class User(AbstractUser):

    class Meta(AbstractUser.Meta):
        swappable = "AUTH_USER_MODEL"

class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.name}:{self.category}'


class Articles(models.Model):
    SCHEMA = {
        'type': 'array',  # a list which will contain the items
        'items': {
            'type': 'string',  # items in the array are strings
        }
    }

    name = models.CharField(max_length=500)
    img = models.ImageField()
    description = models.TextField()
    article = RichTextUploadingField()
    tags = models.ManyToManyField('Tag')
    links = JSONField(schema=SCHEMA, blank=True, null=True)
    files = models.FileField(upload_to="uploads/", blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
