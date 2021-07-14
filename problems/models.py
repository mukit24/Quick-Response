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
    title = models.CharField(max_length=120)
    body = RichTextUploadingField()
    created_on = models.DateTimeField(default=datetime.now)
    last_modified = models.DateTimeField(default=datetime.now)
    tag = models.ManyToManyField('Tag', related_name='problems')
    is_solved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title


class Solution(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    body = RichTextUploadingField()
    created_on = models.DateTimeField(default=datetime.now)
    last_modified = models.DateTimeField(default=datetime.now)
    rating = models.DecimalField(default=0,decimal_places=2,max_digits=10)
    # user_count = models.IntegerField(default=0)
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.problem.title

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    c_body = models.TextField()
    created_on = models.DateTimeField(default=datetime.now)
    last_modified = models.DateTimeField(default=datetime.now)
    problem = models.ForeignKey('Problem', on_delete=models.CASCADE,blank=True,null=True,related_name='cmts_p')
    solution = models.ForeignKey('Solution', on_delete=models.CASCADE,blank=True,null=True)
    
    def __str__(self):
        return self.c_body
