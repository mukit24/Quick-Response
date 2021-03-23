from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
from datetime import datetime, timedelta

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Problem(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=60)
    body = RichTextUploadingField()
    created_on = models.DateTimeField(default=datetime.now)
    last_modified = models.DateTimeField(default=datetime.now)
    tag = models.ManyToManyField('Tag', related_name='problems')
    is_solved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title