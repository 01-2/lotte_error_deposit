from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class patchBoard(models.Model):
    subject = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    created_date = models.DateField(null=True, blank=True)
    memo = models.CharField(max_length=1000, blank=True)
    hits = models.PositiveIntegerField(null=True, blank=True)
    description = RichTextUploadingField(null=True, blank=True)