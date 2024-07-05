from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField
class Lab(models.Model):
    lab_title=models.CharField(max_length=100)
    lab_desc=HTMLField()
    lab_image=models.FileField(upload_to="lab/",max_length=250,null=True,default=None)
    lab_slug=AutoSlugField(populate_from='lab_title',unique=True,null=True,default=None)

# Create your models here.
